import sys
import os

# 1. เพิ่มการดึง Path ของโฟลเดอร์ src เพื่อให้ import โมดูลได้บน Mac/Linux
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# 2. นำเข้า Class ที่เราสร้างไว้จาก Sprint 2-3
from flower_manager import FlowerManager
from cli_interface import CLIInterface

def main():
    # 3. สร้าง Instance ของ FlowerManager และ CLIInterface
    manager = FlowerManager()
    cli = CLIInterface(manager)

    # 4. ใช้ while True เพื่อให้เมนูทำงานวนลูป ไม่เด้งออกจากโปรแกรมทันที
    while True:
        print("=" * 45)
        print("       🌷 FLOWER SHOP MANAGER")
        print("=" * 45)
        print()
        print("ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย")
        print()
        print("1. Search Flowers (ค้นหาและกรองข้อมูล)")
        print("2. Flower Management (เพิ่ม/ลบ/อัปเดตสต็อก)")
        print("3. Sales Statistics (เรียงลำดับและดูรายงาน)")
        print("0. Exit")

        choice = input("\nเลือกเมนู: ").strip()

        # 5. เชื่อมต่อทางเลือกเมนูกับฟังก์ชันใน cli_interface
        if choice == "1":
            cli._search_menu()
        elif choice == "2":
            self_management_submenu(cli)
        elif choice == "3":
            cli._sort_menu()
        elif choice == "0":
            print("\nขอบคุณที่ใช้บริการระบบจัดการร้านดอกไม้!")
            break  # หลุดจากลูปเพื่อออกจากโปรแกรม
        else:
            print("\n[เตือน] ไม่พบเมนูที่เลือก กรุณาเลือก 0-3 เท่านั้น\n")


def self_management_submenu(cli):
    """เมนูย่อยสำหรับการจัดการดอกไม้ (เพิ่ม/ปรับสต็อก/ลบ)"""
    print("\n--- ระบบจัดการดอกไม้ ---")
    print("1. เพิ่มรายการดอกไม้ใหม่")
    print("2. ปรับปรุงสต็อกสินค้า")
    print("3. ลบรายการดอกไม้")
    print("4. แสดงรายการทั้งหมด")
    sub_choice = input("เลือกเมนูย่อย (1-4): ").strip()

    if sub_choice == "1":
        cli._add_flower_menu()
    elif sub_choice == "2":
        cli._update_stock_menu()
    elif sub_choice == "3":
        cli._delete_flower_menu()
    elif sub_choice == "4":
        cli._show_flowers(cli.manager.flowers, "รายการดอกไม้ทั้งหมดในร้าน")
    else:
        print("[เตือน] เลือกเมนูไม่ถูกต้อง")


if __name__ == "__main__":
    main()