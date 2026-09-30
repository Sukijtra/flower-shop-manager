# PLAN.md — แผนงานและข้อกำหนดความสำเร็จ

**โปรเจกต์:** Flower Shop Manager — ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย  
**รายวิชา:** CP352301 Script Programming · ภาคการศึกษา 1/2569 · Group Section 2  
**อาจารย์ผู้สอน:** ผศ. บุญสืบ ไวคำ

---

## 1. ขอบเขตระบบ (System Scope)

โปรแกรม Desktop/CLI สำหรับจัดการร้านดอกไม้ โดยเชื่อมต่อข้อมูลชนิดและรายละเอียดดอกไม้ผ่าน **Public Flower API Gateway** บันทึกข้อมูลสินค้า การขาย และประวัติการทำรายการลง **SQLite Database** อัตโนมัติ พร้อมระบบค้นหา จัดการคลังสินค้า คำนวณสถิติการขาย ออกรายงาน และแสดงผลกราฟวิเคราะห์ข้อมูล

**หน้าจอ/เมนูหลักทั้งหมด 6 ส่วน**

| หน้าจอ/เมนู | หน้าที่ |
|---|---|
| เมนูหลัก (Main Menu) | แถบสถานะระบบ สรุปยอดภาพรวม และทางเข้าสู่เมนูแต่ละส่วน |
| ค้นหาดอกไม้ (Search Flowers) | ค้นหาข้อมูลดอกไม้จาก API/DB ตามชื่อ ประเภท หรือคุณลักษณะ |
| จัดการคลังดอกไม้ (Flower Management) | เพิ่ม แก้ไข ลบ และดูรายการดอกไม้ในคลังสินค้า (CRUD) |
| จัดการการขาย (Sales Management) | บันทึกการสั่งซื้อ คำนวณราคารวม และตัดสต็อกสินค้า |
| สถิติและกราฟ (Statistics & Analytics) | สรุปยอดขาย ดอกไม้ขายดี และสร้างกราฟวิเคราะห์ข้อมูลด้วย Matplotlib |
| ประวัติและส่งออกข้อมูล (History & Export) | ดูประวัติการทำรายการย้อนหลัง และส่งออกรายงานเป็นไฟล์ CSV |

---

## 2. ภาพรวมแผน 3 สปรินต์

| สปรินต์ | เวอร์ชัน | สัปดาห์ | จุดเน้น | สถานะ |
|---|---|---|---|---|
| Sprint 1 | v0.1.0 | 12 | Core Architecture, API Gateway & Basic CLI | เสร็จแล้ว |
| Sprint 2 | v0.2.0 | 13 | Database Persistence, CRUD & Sales Management | เสร็จแล้ว |
| Sprint 3 | v1.0.0 | 14-15 | Data Visualization, Export & Final Refinement | เสร็จแล้ว |

**การหมุนเวียนบทบาทสมาชิกในทีม** — หมุนเวียนหน้าที่ Planner/Architect, Coder/Dev และ Debugger/QA ครบทุกคนตลอด 3 สปรินต์

| สปรินต์ | Planner / Architect | Coder / Dev | Debugger / QA |
|---|---|---|---|
| Sprint 1 | รพีพรรณ (มีน) | สุกิจตรา (องุ่น) | วิยดา (วิว) · ศุภกร (แม็ก) |
| Sprint 2 | วิยดา (วิว) · ศุภกร (แม็ก) | รพีพรรณ (มีน) | สุกิจตรา (องุ่น) |
| Sprint 3 | สุกิจตรา (องุ่น) | วิยดา (วิว) · ศุภกร (แม็ก) | รพีพรรณ (มีน) |

| สมาชิก | ชื่อเล่น | รหัสนักศึกษา | เคยเป็น Planner | เคยเป็น Coder | เคยเป็น QA |
|---|---|---|---|---|---|
| นางสาวรพีพรรณ ศรีบุญเรือง | มีน | 66xxxxxxxx-x | Sprint 1 | Sprint 2 | Sprint 3 |
| นางสาวสุกิจตรา โคแสงรักษา | องุ่น | 66xxxxxxxx-x | Sprint 3 | Sprint 1 | Sprint 2 |
| นางสาววิยดา มูลกัน | วิว | 66xxxxxxxx-x | Sprint 2 | Sprint 3 | Sprint 1 |
| นายศุภกร กงชา | แม็ก | 66xxxxxxxx-x | Sprint 2 | Sprint 3 | Sprint 1 |

---

## 3. Reproducible Artifact Readiness Check

ตรวจสอบความพร้อมขององค์ประกอบพื้นฐานในการพัฒนาและการทำงานร่วมกันภายในทีม

| Artifact | สถานะ | รายละเอียด / สิ่งที่ต้องทำ |
|---|---|---|
| **Project Repository** | พร้อม | Git Repository มี `README.md` อธิบายโครงสร้างและวิธีใช้งานโปรเจกต์ |
| **Virtual Environment** | พร้อม | ใช้ `venv` ของ Python 3.11+ และเพิ่ม `venv/` เข้า `.gitignore` แล้ว |
| **Dependency List** | พร้อม | `requirements.txt` — `requests`, `pytest`, `flake8`, `matplotlib` (SQLite3 เป็น Standard Library) |
| **API Gateway / Config** | พร้อม | เชื่อมต่อ Public Flower API ไม่ต้องใช้ API Key / มี Mock Data สำรอง |
| **Initial Code Structure** | พร้อม | `src/` · `tests/` · `data/` · `reports/` · `tools/` · `.github/workflows/` |
| **CI Pipeline** | พร้อม | `.github/workflows/ci.yml` รัน `flake8` และ `pytest` ทุกการ Push / PR |
| **Test Suite** | พร้อม | ครอบคลุม Unit Test สำหรับ API, DB Management, Sales Calculation และ Validators |
| **Database Schema** | พร้อม | `data/flower_shop.db` สร้างตาราง `flowers`, `orders`, `order_items` อัตโนมัติ |
| **Demo & Seed Data** | พร้อม | มีระบบ `--demo` และไฟล์ Seed Data สำหรับทดสอบระบบทันที |
| **License & Contributor Docs** | พร้อม | มีไฟล์ `LICENSE` (MIT) และ `CONTRIBUTING.md` |
| **UML Class Diagram** | พร้อม | แผนผัง Mermaid แยกตามชั้นสถาปัตยกรรม (Domain, Data/API, UI) |
| **Test Coverage Report** | พร้อม | รวมขั้นตอนวัด Code Coverage เข้าสู่ CI Pipeline |

---

## 4. One-Day Prototype Sprint

กรอบการทำงานเพื่อพิสูจน์แนวคิดและองค์ประกอบทางเทคนิคพื้นฐาน (Proof of Concept)

### I. Setup & Scaffolding

| กิจกรรม | สิ่งที่ต้องส่งมอบ | ผลจริง |
|---|---|---|
| Repository & Structure | สร้างโครงสร้างโฟลเดอร์ `src/`, `tests/`, `data/`, `reports/` | เสร็จ |
| Environment Setup | สร้างและเปิดใช้งาน `venv` | เสร็จ |
| Dependencies | ติดตั้ง `requests`, `pytest`, `flake8` และสร้าง `requirements.txt` | เสร็จ |
| Guard Rails | ตั้งค่า `.gitignore` และ `.flake8` ป้องกัน Cache / DB หลุดเข้า Git | เสร็จ |

### II. API & Database Integration

| กิจกรรม | สิ่งที่ต้องส่งมอบ | ผลจริง |
|---|---|---|
| API Client Setup | สร้าง `FlowerAPIClient` เพื่อดึงข้อมูลดอกไม้จาก Public REST API | เสร็จ |
| Database Setup | สร้าง `DatabaseManager` สำหรับสร้างตาราง SQLite อัตโนมัติ | เสร็จ |
| Integration Test | ทดสอบการดึงข้อมูลจาก API มาบันทึกลง SQLite Database | เสร็จ |
| API Test & Fallback | ทำ Mock HTTP สำหรับทดสอบกรณี Offline / API Failure | ผ่าน |

### III. Core Function & Business Logic

| กิจกรรม | สิ่งที่ต้องส่งมอบ | ผลจริง |
|---|---|---|
| Domain Models | ออกแบบ คลาส `Flower`, `Order`, `SalesManager` | เสร็จ |
| CLI Interface | สร้างเมนูแบบโต้ตอบผ่าน Terminal พร้อมระบบตรวจสอบ Validation | เสร็จ |
| Automated Testing | เขียน Test Suite ด้วย `pytest` ทดสอบ Logic และ DB CRUD | ผ่าน |

---

## 5. Sprint 1 — Core Architecture & API Gateway (v0.1.0)

**เป้าหมาย:** วางโครงสร้างสถาปัตยกรรมระบบ สร้าง Flower API Gateway และระบบ CLI พื้นฐาน

### บทบาทในสปรินต์นี้
* **Planner / Architect:** รพีพรรณ (มีน) — กำหนดโครงสร้างคลาส หน้าที่แต่ละ โมดูล และ DoD
* **Coder / Dev:** สุกิจตรา (องุ่น) — พัฒนา `FlowerAPIClient`, `cli.py` และ `validators.py`
* **Debugger / QA:** วิยดา (วิว) · ศุภกร (แม็ก) — เขียน Unit Tests สำหรับ API Client และ Validation, ตั้งค่า CI Workflow

### Definition of Done

| # | เงื่อนไข | ตรวจด้วยเทสต์ | สถานะ |
|---|---|---|---|
| 1.1 | เมนูหลักรับคำสั่งถูกต้อง และทำงานวนลูปโดยไม่ crash เมื่อกรอกผิด | `test_cli_menu_navigation` | ผ่าน |
| 1.2 | `validators.py` ตรวจสอบ Input ราคา/จำนวน ต้องเป็นตัวเลขบวกเท่านั้น | `test_validate_positive_number` | ผ่าน |
| 1.3 | ดึงข้อมูลดอกไม้จาก Flower API ได้ถูกต้องและแปลงเป็น Domain Model ได้ | `test_api_fetch_flowers` | ผ่าน |
| 1.4 | เมื่อ API ล่ม หรือไม่มีอินเทอร์เน็ต ระบบต้องสลับไปใช้ Mock Data อัตโนมัติ | `test_api_fallback_mechanism` | ผ่าน |
| 1.5 | แยกชั้น UI, Logic และ Data Access ออกจากกันโดยเด็ดขาด | Review Code Design | ผ่าน |

---

## 6. Sprint 2 — Database Persistence & Sales Management (v0.2.0)

**เป้าหมาย:** พัฒนาระบบฐานข้อมูล SQLite, การจัดการคลังดอกไม้ (CRUD) และระบบบันทึกการขาย

### บทบาทในสปรินต์นี้
* **Planner / Architect:** วิยดา (วิว) · ศุภกร (แม็ก) — ออกแบบ DB Schema, ER-Diagram และกฎการตัดสต็อก
* **Coder / Dev:** รพีพรรณ (มีน) — พัฒนา `DatabaseManager`, `FlowerRepository` และ `SalesManager`
* **Debugger / QA:** สุกิจตรา (องุ่น) — ทดสอบ SQLite Transactions, Edge Cases (สินค้าหมด, เงินไม่พอ)

### Definition of Done

| # | เงื่อนไข | ตรวจด้วยเทสต์ | สถานะ |
|---|---|---|---|
| 2.1 | สร้างตาราง SQLite (`flowers`, `orders`) อัตโนมัติเมื่อเริ่มโปรแกรม | `test_db_initialization` | ผ่าน |
| 2.2 | สามารถ เพิ่ม แก้ไข ค้นหา และลบข้อมูลดอกไม้ลง SQLite ได้ (CRUD) | `test_flower_crud_operations` | ผ่าน |
| 2.3 | บันทึกรายการขาย ตัดจำนวนสต็อกดอกไม้อัตโนมัติ และคำนวณราคารวมถูกต้อง | `test_create_order_and_stock_deduction` | ผ่าน |
| 2.4 | ปฏิเสธการขายเมื่อจำนวนสินค้าในสต็อกไม่พอ พร้อมแจ้งเตือนข้อผิดพลาด | `test_insufficient_stock_error` | ผ่าน |
| 2.5 | คำนวณสถิติยอดขายรวม สถิติแยกตามประเภท และดอกไม้ขายดีได้ถูกต้อง | `test_sales_statistics_calculation` | ผ่าน |

---

## 7. Sprint 3 — Data Visualization & Export (v1.0.0)

**เป้าหมาย:** เพิ่มระบบกราฟวิเคราะห์ข้อมูล Matplotlib, การส่งออกไฟล์ CSV, Demo Mode และสรุปโปรเจกต์

### บทบาทในสปรินต์นี้
* **Planner / Architect:** สุกิจตรา (องุ่น) — ออกแบบ Dashboard สรุปผล กราฟวิเคราะห์ และรายงาน CSV
* **Coder / Dev:** วิยดา (วิว) · ศุภกร (แม็ก) — พัฒนา `ReportGenerator`, `ChartVisualizer` และ `--demo` Mode
* **Debugger / QA:** รพีพรรณ (มีน) — ทำ E2E Testing, ตรวจสอบ Coverage > 85%, จัดทำ UML Diagram

### Definition of Done

| # | เงื่อนไข | ตรวจด้วยเทสต์ | สถานะ |
|---|---|---|---|
| 3.1 | สร้างกราฟยอดขาย และกราฟเปรียบเทียบดอกไม้ขายดีด้วย Matplotlib ได้ | `test_chart_generation` | ผ่าน |
| 3.2 | ส่งออกข้อมูลประวัติการขายและสรุปสถิติเป็นไฟล์ CSV ได้ถูกต้อง | `test_export_sales_to_csv` | ผ่าน |
| 3.3 | รองรับคำสั่ง `--demo` เพื่อสาธิตการทำงานของระบบแบบอัตโนมัติ | `test_demo_mode_execution` | ผ่าน |
| 3.4 | โค้ดทั้งหมดผ่านการตรวจ Linting (`flake8`) โดยไม่มี Issue | `flake8 .` | ผ่าน |
| 3.5 | ชุดการทดสอบ Automated Tests ผ่านทั้งหมด 100% บน CI Pipeline | GitHub Actions | ผ่าน |

---

## 8. สถาปัตยกรรม (Separation of Concerns)

```text
main.py                   จุดเริ่มต้นโปรแกรม (รองรับ --demo)
   |
   v
src/cli.py                Presentation Layer — การจัดการเมนูและการรับคำสั่งจากผู้ใช้
   |
   +--> src/ui.py         Presentation Layer — แสดงผลข้อความ ตาราง และรูปแบบสี
   +--> src/validators.py Validation Layer   — ตรวจสอบความถูกต้องของ Input (ไม่มี Print/Input)
   +--> src/models.py     Domain Layer       — Data Classes (Flower, Order, OrderItem)
   +--> src/sales.py      Domain Logic Layer — กฎการขาย การตัดสต็อก และคำนวณสถิติ
   +--> src/reports.py    Reporting Layer    — สร้างรายงานสรุป และส่งออกไฟล์ CSV
   +--> src/charts.py     Visualization Layer— วาดกราฟด้วย Matplotlib
   +--> src/api_gateway.py Integration Layer — เชื่อมต่อ Public Flower API (พร้อม Mock Fallback)
   +--> src/database.py   Data Access Layer  — บันทึก/อ่าน ข้อมูล SQLite Database

## 9. UML Class Diagram

```mermaid
classDiagram
    direction LR

    class Flower {
        +int id
        +str name
        +str category
        +float price
        +int stock
        +str description
        +to_dict()
        +from_dict(data)$
    }

    class OrderItem {
        +Flower flower
        +int quantity
        +float subtotal
    }

    class Order {
        +int id
        +str order_date
        +list~OrderItem~ items
        +float total_amount
        +calculate_total()
    }

    class SalesManager {
        -DatabaseManager db
        +create_order(items)
        +get_sales_summary()
        +get_best_sellers(limit)
    }

    class DatabaseManager {
        -str db_path
        +init_db()
        +add_flower(flower)
        +get_all_flowers()
        +update_stock(flower_id, qty)
        +save_order(order)
    }

    class FlowerAPIGateway {
        -str api_url
        +fetch_remote_flowers()
        +get_fallback_data()
    }

    Order "1" o-- "*" OrderItem : contains
    OrderItem "*" o-- "1" Flower : references
    SalesManager ..> DatabaseManager : uses
    SalesManager ..> Order : manages
    DatabaseManager ..> Flower : stores
## 10. Data Model & Database Schema

ใช้ **SQLite Database** (`data/flower_shop.db`) ในการจัดเก็บข้อมูลหลัก

### 10.1 Schema: `flowers` (ตารางข้อมูลดอกไม้)

| ฟิลด์ | ชนิด | ข้อกำหนด | ความหมาย |
|---|---|---|---|
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | รหัสอ้างอิงดอกไม้ |
| `name` | `TEXT` | `NOT NULL` | ชื่อดอกไม้ |
| `category` | `TEXT` | `NOT NULL` | ประเภทดอกไม้ (เช่น Rose, Lily, Orchid) |
| `price` | `REAL` | `NOT NULL` | ราคาขายต่อหน่วย |
| `stock` | `INTEGER` | `NOT NULL DEFAULT 0` | จำนวนสินค้าในคลัง |
| `description` | `TEXT` | `NULL` | รายละเอียด/คำอธิบาย |

### 10.2 Schema: `orders` (ตารางประวัติการขาย)

| ฟิลด์ | ชนิด | ข้อกำหนด | ความหมาย |
|---|---|---|---|
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | รหัสใบสั่งซื้อ |
| `order_date` | `TEXT` | `NOT NULL` | วันที่และเวลาที่ทำรายการ |
| `total_amount` | `REAL` | `NOT NULL` | ราคารวมทั้งสิ้น |

---

## 11. กลยุทธ์การทดสอบ (Testing Strategy)

เน้นการทดสอบแบบเปิดเครื่องรันอัตโนมัติ (Automated Testing) ที่ทำงานรวดเร็วและไม่ขึ้นกับปัจจัยภายนอก

| ส่วนที่ทดสอบยาก | วิธีแก้ไข / กลยุทธ์ที่ใช้ |
|---|---|
| **การเชื่อมต่อ External API** | ใช้ Mocking Object และ Fallback Dataset เพื่อทดสอบ API Client โดยไม่ต้องพึ่งพาทราฟฟิกเครือข่ายจริง |
| **การใช้งาน SQLite DB** | ใช้ In-Memory SQLite Database (`:memory:`) สำหรับการรัน Test Suite เพื่อความรวดเร็วและไม่สร้างไฟล์ขยะ |
| **ส่วนการแสดงผล CLI** | แยก Validation Logic ออกจาก UI (`validators.py`) เพื่อให้สามารถรัน Unit Test ค่า Input ต่างๆ ได้โดยตรง |
| **การสร้างไฟล์ / กราฟ** | ใช้ `tmp_path` fixture ของ Pytest ในการทดสอบการส่งออก CSV และการ Rendering ภาพกราฟ |

---

## 12. สรุปผลการทดสอบและการทำงานระบบ

| การทดสอบ / โมดูล | ไฟล์ทดสอบ | จำนวนเคส | สถานะ |
|---|---|---|---|
| API Gateway & Fallback | `tests/test_api.py` | 12 | ผ่านทั้งหมด |
| Input Validation | `tests/test_validators.py` | 18 | ผ่านทั้งหมด |
| Database & CRUD Operations | `tests/test_database.py` | 25 | ผ่านทั้งหมด |
| Sales Logic & Stock Management | `tests/test_sales.py` | 20 | ผ่านทั้งหมด |
| Report & Chart Generator | `tests/test_reports.py` | 15 | ผ่านทั้งหมด |
| **รวมทั้งสิ้น** | **5 ไฟล์** | **90 เคส** | **Passed 100% · Flake8 0 Issues** |