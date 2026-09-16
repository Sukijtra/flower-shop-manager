# 🌷 Flower Shop Manager

ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย

**รายวิชา:** CP352301 การเขียนโปรแกรมสคริปต์ (1/2569)
**หัวข้อ:** Flower Shop Manager — ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย
**อาจารย์ผู้สอน:** ผศ. บุญสืบ ไวคำ

---

## 👥 สมาชิกในทีม

| สมาชิก                           | ชื่อเล่น        | Sprint 1            | Sprint 2            | Sprint 3            |
| นางสาวรพีพรรณ ศรีบุญเรือง           | มีน           | Planner / Architect | Coder / Dev         | Debugger / QA       |
| นางสาวสุกิจตรา โคแสงรักษา          | องุ่น          | Coder / Dev         | Debugger / QA       | Planner / Architect |
| นางสาววิยดา มูลกัน                 | วิว           | Debugger / QA       | Planner / Architect | Coder / Dev         |
| นายศุภกร กงชา                    | แม็ก          | Debugger / QA       | Planner / Architect | Coder / Dev         |
> ทีมแบ่งหน้าที่แบบ Role Rotation เพื่อให้สมาชิกทุกคนได้ฝึกทั้งการวางแผน การพัฒนา และการทดสอบระบบ

---

# ✨ สรุปฟีเจอร์ทั้งหมดของระบบ

## 🟢 ฟีเจอร์ที่พัฒนาเสร็จแล้ว

### 🌐 1. Flower API Gateway

ระบบเชื่อมต่อ Flower API เพื่อดึงข้อมูลดอกไม้มาใช้งานภายในโปรแกรม เช่น

* ชื่อดอกไม้
* ประเภทดอกไม้
* ราคา
* รายละเอียด
* รูปภาพดอกไม้
* ข้อมูลที่เกี่ยวข้องกับดอกไม้

มีการแยกส่วน API Gateway ออกจากส่วนอื่นของโปรแกรม เพื่อให้สามารถแก้ไขหรือเปลี่ยน API ได้ง่าย

---

### 💾 2. SQLite Database

ระบบจัดเก็บข้อมูลภายใน SQLite Database เพื่อเก็บข้อมูลอย่างถาวร เช่น

* ข้อมูลดอกไม้
* ราคา
* ประเภทดอกไม้
* จำนวนสินค้า
* ข้อมูลการขาย
* ประวัติการทำรายการ

ฐานข้อมูลจะถูกสร้างและจัดการผ่าน Python โดยไม่จำเป็นต้องติดตั้ง Database Server เพิ่มเติม

---

### 💻 3. Interactive CLI

โปรแกรมสามารถใช้งานผ่าน Command Line Interface โดยมีเมนูสำหรับจัดการระบบ เช่น

```text
========================================
       🌷 FLOWER SHOP MANAGER
========================================

1. Search Flowers
2. Flower Management
3. Sales Management
4. Statistics
5. View History
0. Exit

Select menu:
```

ผู้ใช้สามารถเลือกเมนูและทำงานกับระบบได้โดยตรงผ่าน Terminal

---

### 🔎 4. Flower Search

สามารถค้นหาข้อมูลดอกไม้จากชื่อหรือประเภทที่ต้องการได้

ตัวอย่าง

```text
Search flower: rose

Found 3 flowers

1. Rose
2. Red Rose
3. White Rose
```

ช่วยให้ผู้ใช้สามารถค้นหาข้อมูลดอกไม้ได้สะดวกมากขึ้น

---

### 🌷 5. Flower Management

ระบบจัดการข้อมูลดอกไม้ รองรับการทำงานพื้นฐาน เช่น

* เพิ่มข้อมูลดอกไม้
* แสดงข้อมูลดอกไม้
* ค้นหาดอกไม้
* แก้ไขข้อมูลดอกไม้
* ลบข้อมูลดอกไม้

ข้อมูลทั้งหมดจะถูกบันทึกลง SQLite Database

---

### 📊 6. Sales Statistics

ระบบวิเคราะห์ข้อมูลการขายเบื้องต้น เช่น

* จำนวนรายการขาย
* ยอดขายรวม
* จำนวนดอกไม้ที่ขาย
* ดอกไม้ที่ขายได้มากที่สุด
* ยอดขายแยกตามประเภท
* ราคาเฉลี่ยของสินค้า

ตัวอย่างผลลัพธ์

```text
========================================
          SALES STATISTICS
========================================

Total Orders       : 25
Total Flowers Sold : 48
Total Revenue      : 8,950.00 Baht

Best Selling Flower
-------------------
Rose               : 15
Sunflower          : 10
Lily               : 8
```

---

### 🎬 7. Demo Mode

มี Demo Mode สำหรับใช้สาธิตการทำงานของโปรแกรมโดยไม่ต้องกรอกข้อมูลทีละขั้นตอน

```bash
python main.py --demo
```

เหมาะสำหรับการนำเสนอโปรเจกต์และทดสอบ Flow การทำงานของระบบ

---

### 🧪 8. Automated Tests

ใช้ `pytest` สำหรับทดสอบฟังก์ชันสำคัญของระบบ เช่น

* การเชื่อมต่อ API
* การค้นหาดอกไม้
* การเพิ่มข้อมูล
* การอ่านข้อมูลจาก SQLite
* การคำนวณสถิติ

ตัวอย่างการรัน

```bash
pytest
```

---

# 🟡 Planned Features

ฟีเจอร์ที่วางแผนพัฒนาเพิ่มเติมใน Sprint ถัดไป ได้แก่

### 📄 Report Generator

สร้างรายงานสรุปข้อมูลการขาย เช่น

* รายงานยอดขายประจำวัน
* รายงานยอดขายประจำเดือน
* รายงานดอกไม้ขายดี
* รายงานรายได้รวม

---

### 📈 Matplotlib Data Visualization

นำข้อมูลการขายมาสร้างกราฟด้วย Matplotlib เช่น

* กราฟยอดขายรายวัน
* กราฟยอดขายรายเดือน
* กราฟเปรียบเทียบประเภทดอกไม้
* กราฟดอกไม้ขายดี

---

### 📁 CSV Export

สามารถส่งออกข้อมูลจากระบบเป็นไฟล์ CSV เพื่อให้นำไปวิเคราะห์ต่อใน Excel หรือโปรแกรมอื่นได้

ตัวอย่าง

```text
sales_report.csv
flowers.csv
statistics.csv
```

---

### 🌐 Web Dashboard

พัฒนาหน้าเว็บ Dashboard สำหรับแสดงข้อมูลจากระบบ เช่น

* จำนวนดอกไม้
* จำนวนการขาย
* ยอดขายรวม
* ดอกไม้ขายดี
* กราฟสถิติ

---

# 📅 แผนการทำงานภาพรวม (3 Sprints Roadmap)

## 🌱 Sprint 1: OOP + API + SQLite + CLI

**เป้าหมาย:** สร้างพื้นฐานของระบบและสามารถใช้งานผ่าน Command Line ได้

### รายละเอียดงาน

* ออกแบบโครงสร้างระบบแบบ OOP
* สร้าง Flower API Gateway
* เชื่อมต่อ Flower API
* สร้าง SQLite Database
* สร้างระบบจัดการข้อมูลดอกไม้
* สร้างระบบ Search
* สร้าง CLI Menu
* เพิ่ม Demo Mode
* เขียน Automated Tests

---

## 📊 Sprint 2: Report + Data Analysis

**เป้าหมาย:** เพิ่มความสามารถในการวิเคราะห์ข้อมูลการขาย

### รายละเอียดงาน

* สร้าง Sales Management
* เพิ่มระบบ Statistics
* สร้าง Report Generator
* เพิ่ม Matplotlib
* สร้างกราฟยอดขาย
* วิเคราะห์ดอกไม้ขายดี
* เพิ่ม CSV Export
* เพิ่ม Test Cases

---

## 🌐 Sprint 3: Web Dashboard + GitHub

**เป้าหมาย:** นำข้อมูลจากระบบมาแสดงผลผ่านหน้าเว็บและเตรียมระบบสำหรับการนำเสนอ

### รายละเอียดงาน

* พัฒนา Web Dashboard
* แสดงข้อมูลยอดขาย
* แสดงกราฟสถิติ
* เชื่อมต่อ Database
* ปรับปรุง UI
* ทดสอบระบบทั้งหมด
* จัดทำเอกสาร
* Upload Project ขึ้น GitHub

---

# 🛠️ รายละเอียดการทำงานของระบบ

## 1. OOP Architecture

ระบบแบ่งการทำงานออกเป็นโมดูลเพื่อให้แต่ละส่วนมีหน้าที่ชัดเจน เช่น

```text
Flower API
    ↓
Flower Service
    ↓
Database
    ↓
Sales / Statistics
    ↓
CLI / Web Dashboard
```

การแบ่งส่วนช่วยให้สามารถพัฒนาและแก้ไขแต่ละส่วนได้ง่ายขึ้น

---

## 2. Flower API Gateway

ทำหน้าที่เป็นตัวกลางระหว่างโปรแกรมกับ API

```text
User
 ↓
CLI
 ↓
Flower Service
 ↓
Flower API Gateway
 ↓
External API
```

เมื่อ API ไม่สามารถใช้งานได้ ระบบสามารถจัดการ Error และแจ้งเตือนผู้ใช้แทนการทำให้โปรแกรมหยุดทำงาน

---

## 3. Database

ใช้ SQLite สำหรับจัดเก็บข้อมูลภายในระบบ

ตัวอย่างตาราง

```text
flowers
-------------------------
id
name
category
price
description
created_at

sales
-------------------------
id
flower_id
quantity
total_price
sold_at
```

---

# 🧪 Test Results

ระบบมีการทดสอบด้วย `pytest`

ตัวอย่างผลลัพธ์

```text
============================= test session starts =============================

tests/test_api.py ........
tests/test_database.py ....
tests/test_flower.py .....
tests/test_statistics.py ...

============================= XX passed =============================
```

การทดสอบครอบคลุมฟังก์ชันสำคัญของระบบ เช่น

* API
* Database
* Flower Management
* Search
* Sales
* Statistics

---

# 💻 วิธีการติดตั้ง

## 1. Clone Project

```bash
git clone <YOUR_GITHUB_REPOSITORY>
cd Flower-Shop-Manager
```

## 2. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 วิธีการใช้งาน

## รันโปรแกรมแบบ Interactive

```bash
python main.py
```

จากนั้นเลือกเมนูที่ต้องการจาก CLI

---

## รัน Demo Mode

```bash
python main.py --demo
```

ระบบจะทำงานตามขั้นตอนที่เตรียมไว้สำหรับการสาธิต

---

## รัน Automated Tests

```bash
pytest
```

---

# 📁 Project Structure

```text
Flower-Shop-Manager/
│
├── main.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── flower_api.py
│   ├── flower_service.py
│   ├── data_store.py
│   ├── sales.py
│   ├── statistics.py
│   ├── report_generator.py
│   └── cli_app.py
│
├── data/
│   └── flower_shop.db
│
├── reports/
│   └── sales_report.csv
│
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   ├── test_flower.py
│   └── test_statistics.py
│
└── web/
    ├── index.html
    ├── style.css
    └── script.js
```

---

# 🔄 System Flow

```text
              ┌──────────────────┐
              │      User        │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │   CLI / Web UI   │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Flower Service   │
              └───────┬───┬──────┘
                      ↓   ↓
             ┌─────────┐ ┌─────────────┐
             │Flower API│ │ SQLite DB  │
             └─────────┘ └──────┬──────┘
                                 ↓
                       ┌──────────────────┐
                       │ Sales Statistics │
                       └────────┬─────────┘
                                ↓
                       ┌──────────────────┐
                       │ Report / Charts  │
                       └──────────────────┘
```

---

# 🎯 Project Objectives

1. พัฒนาโปรแกรมด้วยภาษา Python โดยใช้แนวคิด OOP
2. เรียนรู้การเชื่อมต่อและเรียกใช้งาน API
3. จัดเก็บข้อมูลด้วย SQLite Database
4. พัฒนาระบบจัดการข้อมูลผ่าน CLI
5. วิเคราะห์ข้อมูลการขายด้วย Python
6. สร้างรายงานและกราฟจากข้อมูล
7. ฝึกการทำงานเป็นทีมด้วย Git และ GitHub
8. ฝึกการทดสอบโปรแกรมด้วย Automated Testing

---

# 🌷 Expected Result

Flower Shop Manager จะช่วยจัดการข้อมูลดอกไม้และข้อมูลการขายให้อยู่ในระบบเดียว โดยผู้ใช้สามารถค้นหาและจัดการข้อมูลดอกไม้ บันทึกข้อมูลการขาย และดูสถิติที่สำคัญได้ นอกจากนี้ยังสามารถนำข้อมูลไปสร้างรายงานและกราฟเพื่อช่วยให้เห็นภาพรวมของการขายได้ชัดเจนมากขึ้น
