class Flower:
    def __init__(self, flower_id: int, name: str, price: float, stock: int, tags: list = None):
        self.id = flower_id
        self.name = name
        self.price = price
        self.stock = stock
        self.tags = tags if tags else []

    def to_dict(self) -> dict:
        return {
            "type": "Flower",
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "tags": self.tags
        }

    def __str__(self):
        tags_str = f" [แท็ก: {', '.join(self.tags)}]" if self.tags else ""
        return f"[ID: {self.id}] {self.name} - ราคา: {self.price:.2f} บาท | สต็อก: {self.stock} ชิ้น{tags_str}"


class FreshFlower(Flower):
    def __init__(self, flower_id: int, name: str, price: float, stock: int, expiry_date: str, tags: list = None):
        super().__init__(flower_id, name, price, stock, tags)
        self.expiry_date = expiry_date  # Format: YYYY-MM-DD

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "FreshFlower"
        data["expiry_date"] = self.expiry_date
        return data

    def __str__(self):
        base = super().__str__()
        return f"{base} | วันหมดอายุ/ความสด: {self.expiry_date}"


class BouquetFlower(Flower):
    def __init__(self, flower_id: int, name: str, price: float, stock: int, arrangement_style: str, tags: list = None):
        super().__init__(flower_id, name, price, stock, tags)
        self.arrangement_style = arrangement_style

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "BouquetFlower"
        data["arrangement_style"] = self.arrangement_style
        return data

    def __str__(self):
        base = super().__str__()
        return f"{base} | รูปแบบจัดช่อ: {self.arrangement_style}"