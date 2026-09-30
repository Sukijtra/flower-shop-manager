# PLAN.md - Documentation Sprint 2-3
**Project:** Flower Shop Manager  
**Course:** CP352301 Script Programming

## 1. System Architecture & Layer Separation
- **Presentation Layer (`src/cli_interface.py` & `main.py`):** จัดการ UI และ Input Validation
- **Business Logic Layer (`src/flower_manager.py` & `src/flower.py`):** OOP Domain Models, Searching, Filtering, Sorting
- **Data Access Layer (`src/data_persistence.py`):** จัดการ JSON File I/O และ Auto Backup System

## 2. Definition of Done (DoD)
- [x] บันทึกและโหลดข้อมูลจากไฟล์ JSON อัตโนมัติเมื่อเกิดการเปลี่ยนแปลง
- [x] ค้นหา กรอง และเรียงลำดับข้อมูลถูกต้อง
- [x] ดักจับ Exception กรณีข้อมูลผิดพลาด (ค่าติดลบ, ตัวอักษรแทนตัวเลข) โดยโปรแกรมไม่พัง

## 3. QA Test Log (Sprint Review)
| Test ID | Input/Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC-01 | ไม่พบไฟล์ JSON เมื่อเริ่มต้น | สร้างไฟล์ชุดข้อมูลใหม่อัตโนมัติ | Pass | PASSED |
| TC-02 | ปรับสต็อกติดลบ (-10) | แจ้งเตือนปฏิเสธข้อมูล | แสดง [Error] | PASSED |
| TC-03 | ลบ ID ที่ไม่มีในระบบ (F999) | แจ้งเตือน Custom KeyError | แสดง [Error] | PASSED |

## 4. Retrospective (Wow! & Whoops!)
- **Wow!:** แยก Architecture Layer ชัดเจน ทำให้การเชื่อมต่อ Full-Stack ใน Sprint 3 ทำได้อย่างรวดเร็ว
- **Whoops!:** ในช่วงแรกไฟล์ JSON เกิดความเสียหายหากปิดโปรแกรมกะทันหัน ได้แก้ไขโดยทำระบบ Backup File (`.bak`)