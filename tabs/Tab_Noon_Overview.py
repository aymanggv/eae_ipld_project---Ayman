import streamlit as st
from PIL import Image

def show():
    st.header("📘 Project Overview")
    st.markdown(""" 
    ### 📦 Noon Orders SQL Analysis

    This project contains SQL-based analysis on a simulated Noon e-commerce orders dataset. It includes table creation and a series of queries to extract meaningful insights about customer behavior, order volumes, product performance, and platform trends.

    ---

    ### 🗂️ Project Structure
    ```
    noon-orders-sql-analysis/
    │
    ├── sql/
    │   ├── create_noon_orders_table.sql       # DDL script to create table
    │   └── noon_orders_analysis.sql           # SQL queries for analysis
    │
    ├── README.md                              # Project overview
    ```
    ---

    ### 🛠️ Tech Stack

    - **SQL** (MySQL or PostgreSQL syntax depending on your environment)
    - **DB Client**: Use any DB visualization tool like DBeaver, pgAdmin, or MySQL Workbench

    ---

    ### 🚀 How to Run

    1. Import the `create_noon_orders_table.sql` into your SQL environment to create the schema.
    2. Insert your data (or adapt queries to a dataset you have).
    3. Run the queries from `noon_orders_analysis.sql` to explore insights.

    ---

    ### 📁 Example Use Cases

    - E-commerce business intelligence dashboards
    - SQL learning & practice project
    - Interview prep (joins, aggregates, group by, etc.)
    - Portfolio demo

    ---

    ### 📊 Key Analysis

    The SQL queries provide insights such as:

    - Total number of orders
    - Orders by city or platform
    - Customer behavior trends (e.g. average basket size)
    - Top-selling products and categories
    - Revenue and order volume over time
    """)

