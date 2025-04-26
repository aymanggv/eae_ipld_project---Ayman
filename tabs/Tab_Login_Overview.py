import streamlit as st
from PIL import Image

def show():
    st.header("📘 Project Overview")
    st.markdown(""" 
    ### 🔐 Login Details SQL Analysis

    This project contains SQL queries designed to analyze user login data. It helps uncover trends in user activity, security insights, platform usage, and more. Ideal for understanding how users interact with digital platforms over time.

    ---

    ### 🗂️ Project Structure

    ```
    login-details-sql-analysis/
    │
    ├── sql/
    │   ├── login_details_data_analysis.sql     # SQL queries to analyze login activity
        └── login_details_ddl.sql               # # DDL script to create table
    │
    ├── README.md                               # Project overview and documentation

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

    ### 📊 Key Analyses

    The SQL queries provide insights such as:

    - Total number of orders
    - Orders by city or platform
    - Customer behavior trends (e.g. average basket size)
    - Top-selling products and categories
    - Revenue and order volume over time

    """)

