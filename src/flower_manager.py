import datetime
from data_persistence import DataPersistence
from flower import Flower, FreshFlower, BouquetFlower

class FlowerManager:
    def __init__(self):
        self.persistence = DataPersistence()
        self.flowers = self.persistence.load_inventory()

    def _get_next_id(self) -> int:
        return max([f.id for f in self.flowers], default=0) + 1

    def add_flower(self, flower) -> Flower:
        flower.id = self._get_next_id()
        self.flowers.append(flower)
        self.persistence.save_inventory(self.flowers)
        return flower

    def delete_flower(self, flower_id: int) -> bool:
        flower = self.get_flower_by_id(flower_id)
        if flower:
            self.flowers.remove(flower)
            self.persistence.save_inventory(self.flowers)
            return True
        return False

    def get_flower_by_id(self, flower_id: int):
        return next((f for f in self.flowers if f.id == flower_id), None)

    def update_stock(self, flower_id: int, quantity_change: int) -> bool:
        flower = self.get_flower_by_id(flower_id)
        if flower:
            flower.stock += quantity_change
            if flower.stock < 0:
                flower.stock = 0
            self.persistence.save_inventory(self.flowers)
            return True
        return False

    # --- Algorithms: Searching, Filtering, Sorting ---
    def search_flowers(self, keyword: str) -> list:
        kw = keyword.lower().strip()
        if not kw:
            return self.flowers
        return [
            f for f in self.flowers
            if kw in f.name.lower() or any(kw in tag.lower() for tag in f.tags)
        ]

    def filter_flowers(self, min_price=None, max_price=None, in_stock_only=False, tag=None, fresh_only=False) -> list:
        result = self.flowers
        
        if min_price is not None:
            result = [f for f in result if f.price >= min_price]
        if max_price is not None:
            result = [f for f in result if f.price <= max_price]
        if in_stock_only:
            result = [f for f in result if f.stock > 0]
        if tag:
            result = [f for f in result if tag.lower() in [t.lower() for t in f.tags]]
        if fresh_only:
            today = datetime.date.today().strftime("%Y-%m-%d")
            result = [f for f in result if isinstance(f, FreshFlower) and f.expiry_date >= today]
            
        return result

    def sort_flowers(self, criterion="id", reverse=False) -> list:
        if criterion == "price":
            key_func = lambda f: f.price
        elif criterion == "name":
            key_func = lambda f: f.name.lower()
        elif criterion == "stock":
            key_func = lambda f: f.stock
        elif criterion == "expiry":
            key_func = lambda f: f.expiry_date if isinstance(f, FreshFlower) else "9999-99-99"
        else:
            key_func = lambda f: f.id

        return sorted(self.flowers, key=key_func, reverse=reverse)