# PLAN.md — แผนงานและข้อกำหนดความสำเร็จ

**โปรเจกต์:** Flower Shop Manager — ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย  
**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ · ภาคปลาย 1/2569 · อาจารย์ผู้สอน: ผศ. บุญสืบ ไวคำ

---

## 1. ขอบเขตระบบ (System Scope)

แอปพลิเคชันจัดการร้านดอกไม้แบบ Full-Stack/CLI ซึ่งเชื่อมต่อ External Flower API สำหรับดึงข้อมูล ดำเนินการจัดเก็บข้อมูลสินค้าและประวัติการขายใน SQLite Database จัดการระบบหลังบ้านและวิเคราะห์สถิติยอดขาย สร้างรายงาน PDF/CSV กราฟ Matplotlib รวมถึงการแสดงผลผ่าน Interactive CLI และ Web Dashboard

**รายการหน้าจอ/ส่วนทำงานหลัก**

| หน้าจอ / โมดูล | หน้าที่การทำงาน |
|---|---|
| Flower API Gateway | เชื่อมต่อ External API เพื่อดึงข้อมูล รูปภาพ และรายละเอียดดอกไม้ |
| SQLite Database & Data Persistence | จัดเก็บข้อมูลดอกไม้ ประวัติการขาย และ Auto-Backup ลงไฟล์ DB/JSON |
| Interactive CLI & Demo Mode | เมนู Interactive Command Line และโหมด `--demo` สำหรับนำเสนอ |
| Sales & Statistics Engine | คำนวณยอดขายรวม ดอกไม้ขายดี และวิเคราะห์สถิติตามหมวดหมู่ |
| Report & Visualization Generator | ส่งออกรายงาน CSV/PDF และสร้างกราฟด้วย Matplotlib |
| Web Dashboard | หน้าเว็บแสดงสรุปยอดขาย สถิติ และกราฟภาพรวมระบบ |

---

## 2. ภาพรวมแผน 3 สปรินต์และการหมุนเวียนบทบาท

| สปรินต์ | เวอร์ชัน | จุดเน้นการพัฒนา | สถานะ |
|---|---|---|---|
| Sprint 1 | v0.1.0 | OOP + API + SQLite + CLI Core & Automated Tests | [เสร็จแล้ว] |
| Sprint 2 | v0.2.0 | Sales Management + Report Generator + Matplotlib & CSV | [กำลังดำเนินงาน] |
| Sprint 3 | v0.3.0 | Web Dashboard + System Refinement + GitHub Documentation | [วางแผนไว้] |

**การหมุนเวียนบทบาทสมาชิกในทีม**

| สปรินต์ | Planner / Architect | Coder / Dev | Debugger / QA |
|---|---|---|---|
| Sprint 1 | รพีพรรณ (มีน) | สุกิจตรา (องุ่น) | วิยดา (วิว) · ศุภกร (แม็ก) |
| Sprint 2 | วิยดา (วิว) · ศุภกร (แม็ก) | รพีพรรณ (มีน) | สุกิจตรา (องุ่น) |
| Sprint 3 | สุกิจตรา (องุ่น) | วิยดา (วิว) · ศุภกร (แม็ก) | รพีพรรณ (มีน) |

---

## 3. Reproducible Artifact Readiness Check

| Artifact | สถานะ | รายละเอียด / สิ่งที่ต้องทำ |
|---|---|---|
| **Project Repository** | [พร้อม] | GitHub Repository: `https://github.com/Sukijtra/flower-shop-manager.git` |
| **Virtual Environment** | [พร้อม] | จัดตั้ง Python `venv` และระบุใน `.gitignore` |
| **Dependency List** | [พร้อม] | ระบุไลบรารีใน `requirements.txt` (`pytest`, `matplotlib`, ฯลฯ) |
| **API Key / Config** | [พร้อม] | ระบบจัดการ API Gateway พร้อม Fallback Handling เมื่อ API ไม่ตอบสนอง |
| **Initial Code Structure** | [พร้อม] | โครงสร้างโฟลเดอร์ `src/`, `data/`, `reports/`, `tests/`, `web/` |
| **CI Pipeline** | [พร้อม] | GitHub Actions Workflows สำหรับรัน Automated Tests |
| **Test Suite** | [พร้อม] | ชุดทดสอบอัตโนมัติด้วย `pytest` (`test_api.py`, `test_database.py`, ฯลฯ) |
| **Save Data / Seed Data** | [พร้อม] | ไฟล์ SQLite Database (`data/flower_shop.db`) และไฟล์ JSON Auto-Backup |
| **UML Class Diagram** | [พร้อม] | ผังโครงสร้างคลาสระบบด้วย Mermaid Diagram |

---

## 4. สถาปัตยกรรมระบบ (Separation of Concerns)

ระบบถูกออกแบบตามหลัก Layered Architecture เพื่อแยกหน้าที่การทำงานออกจากกันอย่างชัดเจน

```mermaid
flowchart TD
    MAIN["<b>main.py</b><br/>จุดเริ่มโปรแกรม (Interactive CLI & --demo Mode)"]
    PRES["<b>Presentation Layer</b><br/>src/cli_app.py / src/web/<br/>(CLI Interface & Web Dashboard UI)"]
    BIZ["<b>Business Logic Layer</b><br/>src/flower_service.py<br/>(Flower Manager, Sales & Statistics)"]
    API["<b>API Gateway</b><br/>src/flower_api.py<br/>(External Flower API Integration)"]
    DATA["<b>Data Access Layer</b><br/>src/data_store.py<br/>(SQLite Database / JSON Persistence)"]
    REPORT["<b>Report & Data Visualization</b><br/>src/report_generator.py<br/>(CSV Export & Matplotlib Charts)"]

    MAIN --> PRES
    PRES --> BIZ
    BIZ --> API
    BIZ --> DATA
    BIZ --> REPORT

---

## 5. UML Class Diagram (Mermaid)

```mermaid
classDiagram
    class Flower {
        +int flower_id
        +str name
        +str category
        +float price
        +str description
        +to_dict() dict
    }

    class FreshFlower {
        +str expiry_date
        +int shelf_life_days
        +is_fresh() bool
    }

    class FlowerAPIGateway {
        +str api_url
        +fetch_flowers() list
        +handle_error() void
    }

    class DataStore {
        +str db_path
        +save_flower(flower) bool
        +load_flowers() list
        +record_sale(sale_data) bool
    }

    class FlowerService {
        -DataStore db
        -FlowerAPIGateway api
        +add_flower(flower) bool
        +search_flowers(query) list
        +process_sale(flower_id, quantity) bool
    }

    class StatisticsEngine {
        +calculate_revenue() float
        +get_best_sellers() list
        +export_csv() bool
        +generate_charts() void
    }

    Flower <|-- FreshFlower : Inherits
    FlowerService "1" o-- "1" DataStore : Uses
    FlowerService "1" o-- "1" FlowerAPIGateway : Calls
    FlowerService "1" *-- "many" Flower : Manages
    StatisticsEngine "1" o-- "1" DataStore : Analyzes Data