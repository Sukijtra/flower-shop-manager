# Changelog

All notable changes to the **Flower Shop Manager — ระบบจัดการร้านดอกไม้และวิเคราะห์ข้อมูลการขาย** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v0.1.0] - Sprint 1: Project Setup & Core Architecture

### Added

* Created Flower Shop Manager project.
* Created Python project structure with `src/`, `tests/`, and `data/`.
* Added OOP architecture for the main system components.
* Added `FlowerAPI` for retrieving flower information from an API.
* Added `DataStore` for SQLite database management.
* Added `FlowerService` for flower search and management.
* Added CLI application for user interaction.
* Added flower search functionality.
* Added flower management functionality.
* Added sales statistics functionality.
* Added Demo Mode for demonstrating the system.
* Added automated tests for database and statistics functions.
* Added project documentation files.

### Planner / Coder / Debugger Roles

| สมาชิก                    | ชื่อเล่น | Role                | หน้าที่                                                                                                   |
| ------------------------- | -------- | ------------------- | --------------------------------------------------------------------------------------------------------- |
| นางสาวรพีพรรณ ศรีบุญเรือง | มีน      | Planner / Architect | Designed the project structure, system architecture, database concept, and Sprint 1 development plan.     |
| นางสาวสุกิจตรา โคแสงรักษา | องุ่น    | Coder / Dev         | Implemented the Python project structure, OOP classes, CLI menu, API integration, and database functions. |
| นางสาววิยดา มูลกัน        | วิว      | Debugger / QA       | Tested system functions, checked input handling, and verified database and statistics operations.         |
| นายศุภกร กงชา             | แม็ก     | Debugger / QA       | Assisted with testing, error checking, and validation of system functionality.                            |

## [v0.2.0] - Sprint 2: Report Generator & Data Analysis

### Added

- Added `SalesManager` module to handle sales transactions and order records.
- Added `ReportGenerator` module to generate daily and monthly sales summary reports.
- Added Matplotlib integration (`ChartVisualizer`) for data visualization (Sales trends, top-selling products, and category breakdown).
- Added CSV Export functionality (`CSVExporter`) to export `sales_report.csv`, `flowers.csv`, and `statistics.csv`.
- Added unit tests for report generation, CSV export, and chart visualizer modules.

### Changed

- Enhanced `Statistics` module to support advanced analytics, best-selling flower rankings, and average price calculations.
- Updated database schema in `DataStore` to support sales history tracking and timestamps.
- Updated CLI menu with options for generating reports, exporting CSV files, and viewing analytical charts.

### Planner / Coder / Debugger Roles

| สมาชิก                     | ชื่อเล่น | Role                | หน้าที่                                                                                                   |
| ------------------------- | -------- | ------------------- | --------------------------------------------------------------------------------------------------------- |
| นางสาวสุกิจตรา โคแสงรักษา | องุ่น    | Debugger / QA       | Tested sales calculation logic, verified CSV file formats, and checked Matplotlib chart rendering.        |
| นางสาววิยดา มูลกัน        | วิว      | Planner / Architect | Designed the data analysis architecture, report formats, CSV exporter specifications, and chart layouts.  |
| นายศุภกร กงชา             | แม็ก      | Planner / Architect | Co-designed the analytics pipeline, statistics algorithms, and planned Sprint 2 delivery milestones.      |
| นางสาวรพีพรรณ ศรีบุญเรือง | มีน      | Coder / Dev         | Implemented `ReportGenerator`, `CSVExporter`, Matplotlib visualization, and updated CLI sales integration.|

---

## [v0.3.0] - Sprint 3: Web Dashboard, Final Testing & GitHub Deployment

### Added

- Added Web Dashboard interface using HTML, CSS, and JavaScript in the `web/` directory.
- Added RESTful API endpoints / database connector to bridge the Python backend with the Web Dashboard.
- Added interactive real-time metrics, charts, and product stock indicators on the web frontend.
- Added comprehensive System Integration Tests combining API Gateway, Database, Analysis, and UI components.
- Added full project documentation, user manuals, and GitHub repository deployment setup.

### Changed

- Refactored core modules to ensure high cohesion and low coupling (Layered Architecture).
- Improved CLI and Web UI error handling, user feedback, and input validation.
- Finalized production-ready SQLite database seed data and initial setup routines.

### Planner / Coder / Debugger Roles

| สมาชิก                     | ชื่อเล่น | Role                | หน้าที่                                                                                                   |
| ------------------------- | -------- | ------------------- | --------------------------------------------------------------------------------------------------------- |
| นางสาวสุกิจตรา โคแสงรักษา | องุ่น    | Planner / Architect | Designed Web Dashboard architecture, UI/UX workflow, system integration strategy, and final presentation.|
| นางสาววิยดา มูลกัน        | วิว      | Coder / Dev         | Developed Web Dashboard frontend (HTML/CSS/JS), connected backend API data, and refined project codebase.|
| นายศุภกร กงชา             | แม็ก      | Coder / Dev         | Co-developed Web UI components, integrated database queries with frontend views, and fixed UI bugs.   |
| นางสาวรพีพรรณ ศรีบุญเรือง | มีน      | Debugger / QA       | Conducted end-to-end integration testing, verified Web Dashboard data accuracy, and prepared GitHub release.|