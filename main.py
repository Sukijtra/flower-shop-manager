def main():
    print("=" * 45)
    print("       🌷 FLOWER SHOP MANAGER")
    print("=" * 45)
    print()
    print("ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย")
    print()
    print("1. Search Flowers")
    print("2. Flower Management")
    print("3. Sales Statistics")
    print("0. Exit")

    choice = input("\nเลือกเมนู: ")

    if choice == "1":
        print("เปิดระบบค้นหาดอกไม้")
    elif choice == "2":
        print("เปิดระบบจัดการดอกไม้")
    elif choice == "3":
        print("เปิดระบบสถิติการขาย")
    elif choice == "0":
        print("ออกจากโปรแกรม")
    else:
        print("ไม่พบเมนูที่เลือก")


if __name__ == "__main__":
    main()