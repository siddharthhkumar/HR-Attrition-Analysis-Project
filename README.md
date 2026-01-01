#  HR Attrition Analysis Pipeline

### Project Overview
An end-to-end data analysis project designed to identify factors contributing to employee attrition. This project simulates a real-world business intelligence workflow, moving from raw CSV data to actionable insights via a SQL warehouse and Power BI dashboard.

### Tech Stack
* **Python (Pandas, SQLAlchemy):** For ETL (Extract, Transform, Load) and data cleaning.
* **MySQL:** For structured data warehousing and complex querying.
* **Power BI:** For interactive visualization and reporting.

### Key Insights
* **Youth Retention Risk:** Employees under 30 have a **27% attrition rate**, double that of mid-career staff.
* **Departmental Trends:** The R&D department suffers the highest volume of turnover (133 employees).
* **Income Correlation:** Data confirms a strong correlation between lower monthly income and higher attrition probability.

### File Structure
* `load_data.py`: The Python script that automates the ETL process.
* `db_connection.py`: Database connectivity module.
* `HR_Attrition_Dashboard.pbix`: The Power BI dashboard file.
