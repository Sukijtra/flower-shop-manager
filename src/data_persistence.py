import json
import os
import shutil
from flower import Flower, FreshFlower, BouquetFlower

class DataPersistence:
    def __init__(self, filepath="data/inventory.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def save_inventory(self, flowers: list) -> bool:
        try:
            data = [f.to_dict() for f in flowers]
            # สำรองไฟล์เดิมก่อนเขียนทับเพื่อความปลอดภัยของข้อมูล
            if os.path.exists(self.filepath):
                shutil.copyfile(self.filepath, f"{self.filepath}.bak")
                
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except IOError as e:
            print(f"[Error] ไม่สามารถบันทึกไฟล์ได้: {e}")
            return False

    def load_inventory(self) -> list:
        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            flowers = []
            for item in data:
                item_type = item.get("type", "Flower")
                tags = item.get("tags", [])
                
                if item_type == "FreshFlower":
                    flower = FreshFlower(item["id"], item["name"], item["price"], item["stock"], item["expiry_date"], tags)
                elif item_type == "BouquetFlower":
                    flower = BouquetFlower(item["id"], item["name"], item["price"], item["stock"], item["arrangement_style"], tags)
                else:
                    flower = Flower(item["id"], item["name"], item["price"], item["stock"], tags)
                
                flowers.append(flower)
            return flowers
        except (json.JSONDecodeError, KeyError) as e:
            print(f"[Warning] ไฟล์ข้อมูลชำรุด หรือรูปแบบไม่ถูกต้อง: {e}")
            bak_path = f"{self.filepath}.bak"
            if os.path.exists(bak_path):
                print("[System] กำลังกู้คืนข้อมูลจากไฟล์สำรอง (.bak)...")
                shutil.copyfile(bak_path, self.filepath)
                return self.load_inventory()
            return []