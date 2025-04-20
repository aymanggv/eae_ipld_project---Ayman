import streamlit as st
from PIL import Image  # To handle image loading

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="Ayman's Portfolio",
    page_icon="📊",
)

# ---------- Header ----------
st.title("🏭 SQL Data Warehouse Project")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repo", "📊 Results / Visuals"])

# ---------- Overview Tab ----------
with tab1:
    st.header("📘 Project Overview")
    st.markdown(""" 
        Welcome to the **Data Warehouse and Analytics Project** repository! 🚀  
        This project demonstrates a comprehensive end-to-end data warehousing and analytics solution, from building a data warehouse to generating actionable insights. Designed as a portfolio project, it highlights industry best practices in data engineering and analytics.
    """)  # Other markdown content in this tab
    st.markdown("""
    ---

    ## 🏗️ Data Architecture

    The data architecture for this project follows Medallion Architecture **Bronze**, **Silver**, and **Gold** layers:
    """)

    # Display the image using Streamlit's `st.image()`
    image = Image.open("data/data_architecture.png")
    st.image(image, caption="Data Architecture", use_container_width=True)

    st.markdown("""
    1. **Bronze Layer**: Stores raw data as-is from the source systems. Data is ingested from CSV Files into SQL Server Database.
    2. **Silver Layer**: This layer includes data cleansing, standardization, and normalization processes to prepare data for analysis.
    3. **Gold Layer**: Houses business-ready data modeled into a star schema required for reporting and analytics.

    ---

    ## 📖 Project Overview

    This project involves:

    1. **Data Architecture**: Designing a Modern Data Warehouse Using Medallion Architecture **Bronze**, **Silver**, and **Gold** layers.
    2. **ETL Pipelines**: Extracting, transforming, and loading data from source systems into the warehouse.
    3. **Data Modeling**: Developing fact and dimension tables optimized for analytical queries.
    4. **Analytics & Reporting**: Creating SQL-based reports and dashboards for actionable insights.

    🎯 This repository is an excellent resource for showcasing expertise in:
    - SQL Development
    - Data Architect
    - Data Engineering  
    - ETL Pipeline Developer  
    - Data Modeling  
    - Data Analytics  

    ---

    ## 🛠️ Important Links & Tools:

    - **[Datasets](datasets/):** Access to the project dataset (CSV files).
    - **[SQL Server Express](https://www.microsoft.com/en-us/sql-server/sql-server-downloads):** Lightweight server for hosting SQL database.
    - **[SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16):** GUI for managing and interacting with databases.
    - **[Git Repository](https://github.com/):** A GitHub account and repository to manage, version, and collaborate on the code efficiently.
    - **[DrawIO](https://www.drawio.com/):** Design data architecture, models, flows, and diagrams.
    - **[Notion](https://www.notion.com/):** All-in-one tool for project management and organization.
    - **[Notion Project Management Steps](https://www.notion.so/Data-Warehouse-Project-1d576057db5f80b4b845c2f7d66ba5b3?pvs=4):** Access to all of the phases of this project and its tasks.

    ---

    ## 🚀 Project Requirements

    ### Building the Data Warehouse (Data Engineering)

    #### Objective
    Develop a modern data warehouse using SQL Server to consolidate sales data, enabling analytical reporting and informed decision-making.

    #### Specifications
    - **Data Sources**: Import data from two source systems (ERP and CRM) provided as CSV files.
    - **Data Quality**: Clean and resolve data quality issues prior to analysis.
    - **Integration**: Combine both sources into a single, user-friendly data model designed for analytical queries.
    - **Scope**: Focus on the latest dataset only; historization of data is not required.
    - **Documentation**: Provide clear documentation of the data model to support both business stakeholders and analytics teams.

    ---

    ### BI: Analytics & Reporting (Data Analysis)

    #### Objective
    Develop SQL-based analytics to deliver detailed insights into:
    - **Customer Behavior**
    - **Product Performance**
    - **Sales Trends**

    These insights empower stakeholders with key business metrics, enabling strategic decision-making.  

    ---

    ## 📂 Repository Structure

    ```
    data-warehouse-project/
    │
    │data_analysis/
    │   ├── exploratory_data_analysis/      # SQL script for exploratory data analysis
    │   ├── advanced_data_analysis/         # SQL script for advanced data analysis
    │
    ├── datasets/                           # Raw datasets used for the project (ERP and CRM data)
    │   ├── source_crm/                     # CSV files for CRM data
    │   ├── source_erp/                     # CSV files for ERP data
    │
    ├── docs/                               # Project documentation and architecture details
    │   ├── etl.drawio                      # Draw.io file shows all different techniquies and methods of ETL
    │   ├── data_architecture.drawio        # Draw.io file shows the project's architecture
    │   ├── data_catalog.md                 # Catalog of datasets, including field descriptions and metadata
    │   ├── data_flow.drawio                # Draw.io file for the data flow diagram
    │   ├── data_models.drawio              # Draw.io file for data models (star schema)
    │   ├── naming-conventions.md           # Consistent naming guidelines for tables, columns, and files
    │
    ├── scripts/                            # SQL scripts for ETL and transformations
    │   ├── bronze/                         # Scripts for extracting and loading raw data
    │   ├── silver/                         # Scripts for cleaning and transforming data
    │   ├── gold/                           # Scripts for creating analytical models
    │
    ├── tests/                              # Test scripts and quality files
    │
    ├── LICENSE                             # License information for the repository
    └── README.md                           # Project overview and instructions
    ```
    ---

    ## 🛡️ License

    This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

    ---

    ## Acknowledgements

    This project was inspired by [Data with Baraa's](https://www.youtube.com/@DataWithBaraa) tutorial on [SQL Data Warehouse from Scratch](https://www.youtube.com/watch?v=9GVqKuTVANE).
    """)



# ---------- GitHub Repo Tab ----------
with tab2:
    st.header("📂 GitHub Repository")
    st.markdown("""
        [🔗 Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

        _You can explore all code, datasets, and documentation there._  
    """)
        
        

# ---------- Results Tab ----------
with tab3:
    st.header("📊 Demo / Output")
    st.write("Coming soon: Visualizations, KPIs, or a data preview will be added here.")

