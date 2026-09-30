# PLAN.md — แผนงานและข้อกำหนดความสำเร็จ

**โปรเจกต์:** FLOWER_SHOP_MANAGER — ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูล  
**รายวิชา:** CP352301 Script Programming · ภาคปลาย 2569 · Section 2

---

## 1. ขอบเขตระบบ (System Scope)

โปรแกรมสำหรับจัดการคลังสินค้าและสถิติของร้านดอกไม้ ผู้ใช้สามารถค้นหา กรอง เรียงลำดับรายการดอกไม้ เพิ่ม/ลบ/แก้ไขสต็อกสินค้า และบันทึกข้อมูลการดำเนินงานได้อย่างคงทน (Data Persistence) ข้อมูลจะถูกประมวลผลผ่าน Business Logic Layer และบันทึกลงไฟล์ JSON อัตโนมัติพร้อมระบบสร้างไฟล์สำรอง (Auto-Backup)

### หน้าจอและเมนูหลักของระบบ
1. **หน้าเมนูหลัก (Main Menu / Dashboard):** แสดงภาพรวมระบบ แถบสถานะ และทางเข้าสู่เมนูย่อย
2. **ระบบค้นหาและกรองข้อมูล (Search & Filter):** ค้นหาชื่อดอกไม้ กรองตามหมวดหมู่ (Category) และช่วงราคา (Price Range)
3. **ระบบจัดการดอกไม้ (Flower Management):** เพิ่มรายการดอกไม้ใหม่ (รองรับทั้งดอกไม้ทั่วไปและดอกไม้สดที่มีวันหมดอายุ) ปรับปรุงสต็อกสินค้า และลบรายการดอกไม้
4. **ระบบสถิติและการเรียงลำดับ (Sales Statistics & Sorting):** แสดงรายงานสถิติ เรียงลำดับสินค้าตามราคาหรือจำนวนสต็อกคงเหลือ

---

## 2. ภาพรวมแผน 4 สปรินต์ (4-Sprint Roadmap)

| สปรินต์ | เวอร์ชัน | สัปดาห์ | จุดเน้น | สถานะ |
| :--- | :---: | :---: | :--- | :---: |
| **Sprint 1** | v0.1.0 | 12 | Front-End App Dev (CLI Framework & Input Validation) | เสร็จแล้ว |
| **Sprint 2** | v0.2.0 | 13 | Back-End App Dev (OOP Models, DAL & Sorting/Filtering) | เสร็จแล้ว |
| **Sprint 3** | v0.3.0 | 14 | Full-Stack App Dev (CLI/GUI Integration & Edge Cases) | เสร็จแล้ว |
| **Final Sprint** | v1.0.0 | 15 | DevOps, CI/CD Pipeline & AI Integration | วางแผนไว้ |

---

## 3. Reproducible Artifact Readiness Check

| Artifact | สถานะ | รายละเอียด / สิ่งที่ต้องทำ |
| :--- | :---: | :--- |
| **Project Repository** | พร้อม | `github.com/Sukijtra/flower-shop-manager` มี `README.md` ฉบับเต็ม |
| **Virtual Environment** | พร้อม | ใช้ `venv` ของ Python 3.x และใส่ `venv/` ไว้ใน `.gitignore` แล้ว |
| **Dependency List** | พร้อม | `requirements.txt` — รองรับ standard libraries และ `pytest` |
| **Initial Code Structure** | พร้อม | มีโครงสร้าง `src/` (คลาสหลัก) และ `main.py` จุดเชื่อมต่อระบบ |
| **CI Pipeline** | พร้อม | `.github/workflows/ci.yml` ตั้งค่ารัน `pytest` และ `flake8` |
| **Seed Data** | พร้อม | `data/inventory.json` ข้อมูลเริ่มต้นรายการดอกไม้ |
| **Save Data Location** | พร้อม | `data/inventory.json` บันทึกอัตโนมัติ และสร้างไฟล์สำรอง `.bak` |

---

## 4. Definition of Done (DoD) แต่ละสปรินต์

### 📌 Sprint 1 — Front-End CLI & Base Setup
- [x] **1.1** โปรแกรมรันผ่าน Terminal และวนลูปรับค่าเมนูได้โดยไม่ crash
- [x] **1.2** เลือกเมนูผิด หรือพิมพ์ตัวอักษร ระบบต้องแสดงข้อความเตือนและถามใหม่
- [x] **1.3** ใช้ `.strip()` จัดการช่องว่าง และดักจับค่าที่ไม่ถูกต้องอย่างเหมาะสม

### 📌 Sprint 2 — Back-End & Data Processing Layer
- [x] **2.1** ออกแบบ OOP Domain Models โดยใช้ Inheritance/Polymorphism (`Flower` และ `FreshFlower`)
- [x] **2.2** ค้นหา (Searching), กรอง (Filtering) และเรียงลำดับ (Sorting) ข้อมูลได้แม่นยำ
- [x] **2.3** บันทึกข้อมูลลงไฟล์ JSON อัตโนมัติเมื่อเกิดการเปลี่ยนแปลง พร้อมระบบกู้คืนไฟล์สำรอง (`.bak`)

### 📌 Sprint 3 — Full-Stack Integration & Edge Cases
- [x] **3.1** เมนู CLI เรียกใช้งานฟังก์ชัน CRUD ฝั่ง Back-End ได้อย่างไร้รอยต่อ
- [x] **3.2** ข้อมูลในหน่วยความจำ (RAM) ตรงกับไฟล์เซฟ JSON ตลอดเวลา (Data Consistency)
- [x] **3.3** ดักจับราคาติดลบ สต็อกติดลบ หรือรหัสสินค้าที่ไม่มีในระบบ โดยแสดง Custom Warning

---

## 5. สถาปัตยกรรมระบบ (Separation of Concerns)

```text
main.py                   (จุดเริ่มต้นโปรแกรม & บังคับ Path การ Import)
   │
   ▼
src/cli_interface.py      [Presentation Layer]
   │                      - รับค่าจากผู้ใช้, แสดงผลเมนู CLI
   │
   ▼
src/flower_manager.py      [Business Logic Layer (BLL)]
   │                      - ประมวลผล Search, Filter, Sort Algorithms
   │
   ├──► src/flower.py     [Domain Models]
   │                      - Flower (Base Class) & FreshFlower (Subclass)
   │
   ▼
src/data_persistence.py   [Data Access Layer (DAL)]
                          - อ่าน/เขียนไฟล์ data/inventory.json
                          - จัดการ Auto-Backup (data/inventory.json.bak)


## 6. UML Class Diagram (Mermaid)

```mermaid
classDiagram
    class Flower {
        +str flower_id
        +str name
        +float price
        +int stock
        +str category
        +to_dict() dict
        +from_dict(data) Flower
    }

    class FreshFlower {
        +str expiry_date
        +to_dict() dict
    }

    class FlowerManager {
        -List~Flower~ flowers
        -DataPersistence persistence
        +add_flower(flower) bool
        +update_stock(flower_id, new_stock) bool
        +delete_flower(flower_id) bool
        +search_by_name(keyword) List~Flower~
        +filter_flowers(category, min_price, max_price) List~Flower~
        +sort_flowers(key, reverse) List~Flower~
    }

    class DataPersistence {
        +str filepath
        +str backup_path
        +save_data(data) bool
        +load_data() List~dict~
    }

    class CLIInterface {
        -FlowerManager manager
        +_search_menu()
        +_add_flower_menu()
    }

    Flower <|-- FreshFlower : Inherits
    FlowerManager "1" *-- "many" Flower : Contains
    FlowerManager "1" o-- "1" DataPersistence : Uses
    CLIInterface "1" o-- "1" FlowerManager : Controls