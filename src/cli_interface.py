import datetime
from flower import Flower, FreshFlower, BouquetFlower

class CLIInterface:
    def __init__(self, manager):
        self.manager = manager

    def display_menu(self):
        print("\n==========================================")
        print("  ระบบจัดการร้านดอกไม้ (Flower Shop CLI)")
        print("==========================================")
        print("1. แสดงรายการดอกไม้ทั้งหมด")
        print("2. เพิ่มรายการดอกไม้ใหม่")
        print("3. ปรับปรุงสต็อกสินค้า (ขาย/เติม)")
        print("4. ลบรายการดอกไม้")
        print("5. ค้นหาดอกไม้ (ชื่อ/แท็กโอกาส)")
        print("6. กรองข้อมูลสินค้า (ราคา/สต็อก/สดใหม่)")
        print("7. เรียงลำดับรายการสินค้า")
        print("0. ออกจากโปรแกรม")
        print("------------------------------------------")

    def run(self):
        while True:
            self.display_menu()
            choice = input("เลือกเมนู (0-7): ").strip()

            try:
                if choice == "1":
                    self._show_flowers(self.manager.flowers, "รายการดอกไม้ทั้งหมดในร้าน")
                elif choice == "2":
                    self._add_flower_menu()
                elif choice == "3":
                    self._update_stock_menu()
                elif choice == "4":
                    self._delete_flower_menu()
                elif choice == "5":
                    self._search_menu()
                elif choice == "6":
                    self._filter_menu()
                elif choice == "7":
                    self._sort_menu()
                elif choice == "0":
                    print("\nขอบคุณที่ใช้บริการระบบจัดการร้านดอกไม้!")
                    break
                else:
                    print("[เตือน] กรุณาเลือกหมายเลขระหว่าง 0 ถึง 7 เท่านั้น")
            except Exception as e:
                print(f"[Error resilience] เกิดข้อผิดพลาดในระบบ: {e}")

    def _get_valid_float(self, prompt: str) -> float:
        while True:
            try:
                val = float(input(prompt))
                if val < 0:
                    print("[เตือน] ค่าต้องไม่ติดลบ กรุณากรอกใหม่")
                    continue
                return val
            except ValueError:
                print("[เตือน] กรุณากรอกตัวเลขที่ถูกต้อง (เช่น 150 หรือ 99.50)")

    def _get_valid_int(self, prompt: str) -> int:
        while True:
            try:
                val = int(input(prompt))
                return val
            except ValueError:
                print("[เตือน] กรุณากรอกตัวเลขจำนวนเต็มเท่านั้น")

    def _get_valid_date(self, prompt: str) -> str:
        while True:
            date_str = input(prompt).strip()
            try:
                datetime.datetime.strptime(date_str, "%Y-%m-%d")
                return date_str
            except ValueError:
                print("[เตือน] รูปแบบวันที่ไม่ถูกต้อง! ต้องเป็น YYYY-MM-DD (เช่น 2026-10-15)")

    def _show_flowers(self, flowers: list, title: str):
        print(f"\n--- {title} (จำนวนทั้งหมด: {len(flowers)} รายการ) ---")
        if not flowers:
            print("ไม่พบข้อมูลสินค้า")
            return
        for f in flowers:
            print(f)

    def _add_flower_menu(self):
        print("\n--- เพิ่มรายการดอกไม้ใหม่ ---")
        print("1. ดอกไม้ทั่วไป/ประดิษฐ์")
        print("2. ดอกไม้สด (มีวันหมดอายุ)")
        print("3. ช่อดอกไม้จัดพิเศษ")
        f_type = input("เลือกประเภทสินค้า (1-3): ").strip()

        name = input("ชื่อดอกไม้/สินค้า: ").strip()
        while not name:
            print("[เตือน] ชื่อสินค้าห้ามว่างเปล่า")
            name = input("ชื่อดอกไม้/สินค้า: ").strip()

        price = self._get_valid_float("ราคา (บาท): ")
        stock = self._get_valid_int("จำนวนในสต็อก: ")

        tags_input = input("แท็ก/โอกาสพิเศษ (คั่นด้วย , เช่น วาเลนไทน์,รับปริญญา): ")
        tags = [t.strip() for t in tags_input.split(",") if t.strip()]

        if f_type == "2":
            expiry = self._get_valid_date("วันหมดอายุ/ความสด (YYYY-MM-DD): ")
            flower = FreshFlower(0, name, price, stock, expiry, tags)
        elif f_type == "3":
            style = input("รูปแบบการจัดช่อ (เช่น มินิมอล, หรูหรา): ").strip()
            flower = BouquetFlower(0, name, price, stock, style, tags)
        else:
            flower = Flower(0, name, price, stock, tags)

        added = self.manager.add_flower(flower)
        print(f"บันทึกข้อมูลเรียบร้อย! รหัสสินค้าคือ [ID: {added.id}]")

    def _update_stock_menu(self):
        f_id = self._get_valid_int("ใส่ ID ดอกไม้ที่ต้องการปรับสต็อก: ")
        change = self._get_valid_int("จำนวนที่ต้องการปรับ (+ เพิ่มสต็อก, - ขาย/ตัดสต็อก): ")
        if self.manager.update_stock(f_id, change):
            print("อัปเดตสต็อกเรียบร้อยแล้ว!")
        else:
            print("[ข้อผิดพลาด] ไม่พบ ID สินค้าดังกล่าวในระบบ")

    def _delete_flower_menu(self):
        f_id = self._get_valid_int("ใส่ ID ดอกไม้ที่ต้องการลบ: ")
        confirm = input(f"ยืนยันการลบสินค้า ID {f_id} หรือไม่? (y/n): ").strip().lower()
        if confirm == 'y':
            if self.manager.delete_flower(f_id):
                print("ลบรายการสินค้าเรียบร้อยแล้ว")
            else:
                print("[ข้อผิดพลาด] ไม่พบ ID สินค้าในระบบ")

    def _search_menu(self):
        kw = input("ป้อนคีย์เวิร์ดที่ต้องการค้นหา (ชื่อสินค้า หรือ แท็กโอกาส): ").strip()
        results = self.manager.search_flowers(kw)
        self._show_flowers(results, f"ผลการค้นหาสำหรับ '{kw}'")

    def _filter_menu(self):
        print("\n--- ตัวเลือกการกรองข้อมูล ---")
        in_stock = input("แสดงเฉพาะสินค้าที่มีในสต็อกหรือไม่? (y/n): ").strip().lower() == "y"
        fresh_only = input("แสดงเฉพาะดอกไม้สดที่ยังไม่หมดอายุหรือไม่? (y/n): ").strip().lower() == "y"
        tag = input("กรองตามแท็กเฉพาะ (เว้นว่างหากไม่ต้องการ): ").strip() or None

        results = self.manager.filter_flowers(in_stock_only=in_stock, fresh_only=fresh_only, tag=tag)
        self._show_flowers(results, "ผลการกรองรายการสินค้า")

    def _sort_menu(self):
        print("\n--- เรียงลำดับรายการ ---")
        print("เงื่อนไขที่รองรับ: id, price, name, stock, expiry")
        crit = input("เรียงตาม (ค่าเริ่มต้น: id): ").strip().lower() or "id"
        rev = input("เรียงจากมากไปน้อย (Descending) หรือไม่? (y/n): ").strip().lower() == "y"

        results = self.manager.sort_flowers(criterion=crit, reverse=rev)
        self._show_flowers(results, f"เรียงลำดับรายการตาม {crit}")

        