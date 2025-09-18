# Customer-Sales

Welcome to the **Customer-Sales** repository!  

This repository provides scripts and data related to analyzing customer and sales data. 
This project demonstrates the ETL(Extract, Transform, Load) activities and data analysis on the customers and sales file.
Designed as a portfolio project, it highlights best practices in data engineering.

## 📊 Project Overview

The project contains Python code for loading, processing, and analyzing sales/customer CSVs, as well as T‑SQL scripts for database‑side operations.  

**`Customer-Sales`**  

├── **`Python Scripts`**  

      - Extract-01 has scripts to extract data from CSV files and load to staging tables  
      
      - Transform_02 has scripts to clean up data from the staging tables  
      
      - Load_03 had scripts to load the cleaned up data to SQL Database (SQL Server DB)  
      
├── **`SQL Scripts`**
      - Data Analysis is used to perfprm basic and necessary analysis on the customer and sales data     
├── **`customers.csv`**
      - Customer dataset
├── **`sales.csv`** 
      - Sales transaction dataset
└── **`README.md`** 
      - Project documentation

## Repository Structure
### 📁 Datasets

- **`customers.csv`** – Sample customer info (IDs, names, etc.)
- **`sales.csv`** – Sales records (transaction ID, customer ID, date, price, etc.)

### 🐍 Python Scripts

Located in `Python Scripts/`, these scripts perform:
- Extracting data from csv files
- Cleaning and transformation
- Loading data to SQL Database

> Dependencies:
- Python 3.x installed  
- Required packages (example): `pandas`, `sqlalchemy`
- Ability to read CSV files

### 🛢 SQL Scripts

Located in `SQL Scripts/`, these scripts include:
- Example SQL queries to analyze customer and sales data
- Joins and filters

> Dependencies:
- Microsoft SQL Server / tool that accepts T‑SQL (e.g. Microsoft SQL Server, Azure SQL)  
- Permissions to create tables / execute queries
