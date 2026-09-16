# 📓 Learning Log & Responsible AI Prompt Record (Flower Shop Manager)

**Project Title:** Flower Shop Manager — ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย

**Team Members & Roles:**

* 👩‍💻 **มีน:** Planner / Architect
* 👩‍💻 **องุ่น:** Coder / Dev
* 👩‍💻 **วิว:** Debugger / QA
* 👨‍💻 **แม็ก:** Debugger / QA

---

## 1. Context & Educational Rationale

เพื่อปฏิบัติตามหลักการ **Responsible AI & Explainable Systems** เอกสารฉบับนี้จัดเก็บคำถาม (Prompt), สรุปคำตอบเชิงทฤษฎีจาก AI และชุดทดสอบ Live Python Code ที่นำมาใช้เป็นแนวทางในการพัฒนาโปรเจกต์ **Flower Shop Manager**

การใช้ AI ในโครงงานเน้นการช่วยอธิบายแนวคิด ให้คำแนะนำด้านการออกแบบ และช่วยตรวจสอบแนวทางการเขียนโปรแกรม โดยสมาชิกในทีมเป็นผู้ตรวจสอบและปรับปรุงโค้ดก่อนนำไปใช้งานจริง

---

## 2. Records of AI Prompts & Responses

### 🔹 Prompt 1: Designing OOP Flower Management System

* **Student Prompt:**

  ```
  ออกแบบระบบจัดการร้านดอกไม้ด้วยภาษา Python ตามหลัก OOP
  โดยมีคลาสสำหรับจัดการข้อมูลดอกไม้ การค้นหาดอกไม้
  และการจัดการข้อมูลสินค้า เช่น ชื่อดอกไม้ ราคา และประเภทดอกไม้
  ```

* **AI Response Summary:**
  แนะนำการแบ่งระบบออกเป็นคลาสตามหน้าที่ เช่น `FlowerService` สำหรับจัดการข้อมูลและการค้นหา และใช้แนวคิด OOP เพื่อให้โค้ดเป็นระบบและสามารถนำกลับมาใช้ได้ง่าย

* **Live Verification Code:**

  ```python
  from src.flower_service import FlowerService

  service = FlowerService()

  flowers = service.search_flowers("rose")

  print("Search Result:", flowers)
  ```

---

### 🔹 Prompt 2: SQLite Database with DataStore

* **Student Prompt:**

  ```
  ออกแบบคลาส DataStore สำหรับจัดการฐานข้อมูล SQLite
  เพื่อบันทึกข้อมูลดอกไม้ เช่น ชื่อดอกไม้ ราคา ประเภท
  และข้อมูลการขาย พร้อมเมธอดสำหรับเพิ่ม แก้ไข ลบ และค้นหาข้อมูล
  ```

* **AI Response Summary:**
  แนะนำการใช้ `sqlite3.connect()` สำหรับเชื่อมต่อฐานข้อมูล SQLite และแบ่งฟังก์ชันการทำงานของฐานข้อมูลออกจากส่วนติดต่อผู้ใช้ เพื่อให้โค้ดดูแลและแก้ไขได้ง่าย

* **Live Verification Code:**

  ```python
  from src.data_store import DataStore

  store = DataStore()

  print("Database Store:", store)
  ```

---

### 🔹 Prompt 3: CLI Interface & Main Controller

* **Student Prompt:**

  ```
  สร้าง CLI Application สำหรับระบบ Flower Shop Manager
  โดยมีเมนูสำหรับค้นหาดอกไม้ จัดการข้อมูลดอกไม้
  และดูสถิติการขาย พร้อมระบบตรวจสอบข้อมูลที่ผู้ใช้ป้อน
  ```

* **AI Response Summary:**
  แนะนำการออกแบบ `CLIApp` เป็นตัวควบคุมการทำงานหลักของโปรแกรม และแบ่งเมนูออกตามหน้าที่ เช่น Search Flowers, Flower Management และ Sales Statistics เพื่อให้ผู้ใช้สามารถใช้งานระบบได้ง่าย

* **Live Verification Code:**

  ```python
  from src.cli_app import CLIApp

  app = CLIApp()

  app.run()
  ```

---

### 🔹 Prompt 4: Flower API Integration

* **Student Prompt:**

  ```
  ออกแบบคลาสสำหรับเชื่อมต่อ Flower API ด้วยภาษา Python
  เพื่อดึงข้อมูลดอกไม้จาก API และนำข้อมูลมาแสดงในระบบ
  โดยต้องมีการจัดการ Exception เมื่อ API ไม่สามารถใช้งานได้
  ```

* **AI Response Summary:**
  แนะนำการใช้ `requests` สำหรับเรียก API และกำหนด `timeout` เพื่อป้องกันโปรแกรมรอนานเกินไป รวมถึงใช้ `try-except` สำหรับจัดการกรณี API เชื่อมต่อไม่ได้หรือเกิดข้อผิดพลาด

* **Live Verification Code:**

  ```python
  from src.flower_api import FlowerAPI

  api = FlowerAPI()

  result = api.search_flowers("rose")

  print("API Result:", result)
  ```

---

### 🔹 Prompt 5: Sales Statistics & Data Analysis

* **Student Prompt:**

  ```
  สร้างระบบวิเคราะห์ข้อมูลการขายร้านดอกไม้
  โดยคำนวณยอดขายรวม จำนวนรายการขาย
  และแสดงข้อมูลในรูปแบบกราฟเพื่อช่วยวิเคราะห์ข้อมูล
  ```

* **AI Response Summary:**
  แนะนำการใช้ `pandas` สำหรับจัดการข้อมูลตาราง และ `matplotlib` สำหรับสร้างกราฟ เช่น กราฟยอดขาย เพื่อช่วยให้เห็นแนวโน้มและสรุปข้อมูลได้ง่ายขึ้น

* **Live Verification Code:**

  ```python
  from src.statistics import Statistics

  statistics = Statistics()

  result = statistics.get_summary()

  print("Sales Statistics:", result)
  ```

---

### 🔹 Prompt 6: Automated Testing

* **Student Prompt:**

  ```
  สร้าง Unit Test สำหรับตรวจสอบการทำงานของระบบ Flower Shop Manager
  โดยทดสอบฐานข้อมูลและฟังก์ชันการคำนวณสถิติการขาย
  ```

* **AI Response Summary:**
  แนะนำการใช้ `pytest` เพื่อสร้าง Automated Tests และแยกไฟ
