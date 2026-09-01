# Decode Labs - Data Analytics Internship

This repository contains my milestone projects completed during the Data Analytics Internship at Decode Labs. The focus of this internship is on transforming raw data into business intelligence, maintaining data integrity, and building reproducible workflows.

## 🚀 Projects Included

### Project 1: Data Cleaning & Preparation 
**Goal:** Clean a raw dataset by handling missing values, duplicates, and incorrect data formatting without compromising statistical power.
* Imputed missing categorical data using Mode values.
* Audited and removed duplicate records based on unique Order IDs.
* Standardized data formats to ISO 8601.
* Applied Python and Pandas to create a fully reproducible data cleaning script.

### Project 2: Exploratory Data Analysis (EDA)
**Goal:** Interrogate cleaned data to uncover hidden patterns, trends, and outliers using analytical logic.
* Conducted univariate analysis using a Five-Number Summary.
* Implemented the Interquartile Range (IQR) method to dynamically detect outliers and identify VIP customer signals.
* Calculated the Pearson Correlation Coefficient to map linear relationships and key revenue drivers.
* Developed a Python pipeline to automate the genration of data-driven Executive Summary 

### Project 3: SQL Data Analysis
**Goal:** Use structured SQL queries to extract actinable business intelligence, filter records, and aggregate performance metrics from raw datasets.
* Engineered a Python-based SQL engine using `sqlite3` and `pandas` to query local `.xlsx` files directly.
* Executed relational `SELECT` queries utilizing `WHERE`, `ORDER BY`, and `GROUP BY` clauses to isolate high-value transactions.
* Performed data aggregation (`COUNT`, `SUM`, `AVG`) to identify top revenue-driving products and quantify a 41.4% order failure transactions.
* Automated the extraction of query results into dynamically formated Markdown reports.

## 🛠️ Tools & Technologies
* **Language:** Python
* **Libraries:** Pandas, Openpyxl, sqlite3
* **Environment:** VS Code, Git