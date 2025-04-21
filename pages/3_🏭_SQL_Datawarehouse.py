import streamlit as st
from PIL import Image  # To handle image loading

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="SQL Data Warehouse Project",
    page_icon="🏭",
)

# ---------- Header ----------
st.title("🏭 SQL Data Warehouse and Data Engineering Project")


# ----- Left menu -----
with st.sidebar:
    st.write("From raw data to insights with clean folders, SQL pipelines (bronze/silver/gold), and solid docs.")
    st.write("###")
    st.write("**Author:** Ayman")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repo", "📊 Results / Visuals"])

# ---------- Overview Tab ----------
with tab1:
    st.header("📘 Project Overview")
    st.markdown(""" 
        Welcome to the **Data Warehouse and Analytics Project** repository! 🚀  
        This project demonstrates a comprehensive end-to-end data warehousing and analytics solution, from building a data warehouse to generating actionable insights. Designed as a portfolio project, it highlights industry best practices in data engineering and analytics.
    """) 
    st.markdown("""
    ---

    ## 🏗️ Data Architecture

    The data architecture for this project follows Medallion Architecture **Bronze**, **Silver**, and **Gold** layers:
    """)

    # Display the image using Streamlit's `st.image()`
    image = Image.open("data/data_architecture.png")
    st.image(image, caption="Data Architecture", use_column_width=True)

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
    
    # Nested tabs inside the main tab
    subtab1, subtab2 = st.tabs(["🔍 Exploratory Data Analysis", "📈 Advanced Analysis"])

    with subtab1:
        st.subheader("🔍 Exploratory Data Analysis")
        st.write("Basic exploration of ERP and CRM data.")
        st.markdown("""
    ---      
    
    1. Explore all the countries our customers come from
    ```sql
    select distinct country 
    from gold.dim_customers;
    ```
    
    | **country**     |
    |-----------------|
    | N/A             |
    | Germany         |
    | United States   |
    | Australia       |
    | United Kingdom  |
    | Canada          |
    | France          |
    
    ---
    
    2. Find date of first and last order and how many years of sales are there.
    ```sql
    select min(order_date) as first_order_date, 
    max(order_date) as last_order_date,
    cast(year(max(order_date)) as int) - cast(year(min(order_date)) as int) as years_of_sales
    from gold.facts_table;
    ```
    
    | **first_order_date** | **last_order_date** | **years_of_sales** |
    |----------------------|---------------------|--------------------|
    | 2010-12-29           | 2014-01-28          | 4                  |
    
    ---
    
    3. Find youngest and oldest customers
    ```sql
    select min(birthdate) as oldest_birthdate,
    datediff(year, min(birthdate), getdate()) as oldest_age,
    max(birthdate) as youngest_bdate,
    datediff(year, max(birthdate), getdate()) as youngest_age
    from gold.dim_customers;
    ```
    
    | **oldest_birthdate** | **oldest_age** | **youngest_birthdate** | **youngest_age** |
    |----------------------|----------------|------------------------|------------------|
    | 1916-02-10           | 109            | 1986-06-25             | 39               |
    
    
    ---
    
    
    4. Find the Total Sales
    ```sql
    select sum(sales_amount) as total_sales
    from gold.facts_table;
    ```
    | **total_sales** |
    |-----------------|
    |    29356250     |
    
    
    ---
    
    
    5. Find how many items are sold
    ```sql
    select sum(quantity) as total_items
    from gold.facts_table;
    ```
    
    | **total_items** |
    |-----------------|
    |     60423       |
    
    
    ---
    
    
    6. Find the average selling price
    ```sql
    select avg(price) as avg_price
    from gold.facts_table
    ```
    
    | **avg_price** |
    |---------------|
    |     486       |


    ---


    7. Find the Total number of Orders
    ```sql
    select count(distinct order_number) as total_orders
    from gold.facts_table
    ;
    ```
    
    | **total_orders** |
    |------------------|
    |     27659        |
    
    
    ---
    
    
    8. Find the total number of products
    ```sql
    select count(distinct product_name) as total_products
    from gold.dim_products
    ```
    
    | **total_products** |
    |--------------------|
    |     295            |
    
    
    ---
    

    9. Find the total number of customers
    ```sql
    select count(customer_key) as total_customers
    from gold.dim_customers
    ```
    
    | **total_customers** |
    |---------------------|
    |     18484           |


    ---

    

    10. Find the total number of customers that have placed an order
    ```sql
    select count(distinct customer_key) as total_cutomers
    from gold.facts_table
    ```
    | **total_customers** |
    |---------------------|
    |     18484           |
    
    
    ---
    
    
    11. Generate a query that shows all key metrics of the business
    ```sql
    select 'Total Sales' as measure_name, sum(sales_amount) as measure_value from gold.facts_table
    union all
    select 'Total Quantity' as masure_name, sum(quantity) as measure_value from gold.facts_table
    union all
    select 'Average Price' as masure_name, avg(price) as measure_value from gold.facts_table
    union all
    select 'Total Orders' as masure_name, count(distinct order_number) as measure_value from gold.facts_table
    union all
    select 'Total Products' as masure_name, count(distinct product_name) as measure_value from gold.dim_products
    union all
    select 'Total Customers' as masure_name, count(customer_key) as measure_value from gold.dim_customers
    union all
    select 'Total Customers Who Bought' as masure_name, count(distinct customer_key) as measure_value from gold.facts_table
    ```
    
    | **measure_name**                | **measure_value** |
    |--------------------------------|--------------------|
    | Total Sales                    | 29356250           |
    | Total Quantity                 | 60423              |
    | Average Price                  | 486                |
    | Total Orders                   | 27659              |
    | Total Products                 | 295                |
    | Total Customers                | 18484              |
    | Total Customers Who Bought     | 18484              |


    ---
    
    
    12. Find total customers by countries
    ```sql
    select country,count(customer_id)  as total_customers
    from gold.dim_customers
    group by country;
    ```

    | **country**        | **total_customers** |
    |--------------------|---------------------|
    | N/A                | 337                 |
    | Germany            | 1780                |
    | United States      | 7482                |
    | Australia          | 3591                |
    | United Kingdom     | 1913                |
    | Canada             | 1571                |
    | France             | 1810                |


    ---


    13. Find total customers by gender
    ```sql
    select gender, count(customer_id) as total_customers
    from gold.dim_customers
    group by gender;
    ```
    | **gender** | **total_customers** |
    |------------|---------------------|
    | N/A        | 15                  |
    | Male       | 9341                |
    | Female     | 9128                |

    
    ---


    14. Find total products by category
    ```sql
    select category, count(product_name) as total_products
    from gold.dim_products
    group by category;
    ```
    | **category** | **total_products** |
    |--------------|--------------------|
    | NULL         | 7                  |
    | Accessories  | 29                 |
    | Bikes        | 97                 |
    | Clothing     | 35                 |
    | Components   | 127                |
    
    
    ---
    
    
    15. What is the average costs in each category?
    ```sql
    select category, avg(cost) as avg_cost
    from gold.dim_products
    group by category;
    ```
    
    | **category**  | **avg_cost** |
    |---------------|--------------|
    | NULL          | 28           |
    | Accessories   | 13           |
    | Bikes         | 949          |
    | Clothing      | 24           |
    | Components    | 264          |

    
    ---
    

    16. What is the total revenue generated for each category?
    ```sql
    select pr.category, sum(sales_amount) as total_revenue
    from gold.facts_table ft
    left join gold.dim_products pr
    on ft.product_key = pr.product_key
    group by pr.category
    ```
    
    | **category**  | **total_revenue** |
    |---------------|-------------------|
    | Accessories   | 700262            |
    | Bikes         | 28316272          |
    | Clothing      | 339716            |


    ---


    17. Find total revenue that is generated by each customer
    ```sql
    select cu.customer_key, cu.first_name, cu.last_name, sum(sales_amount) as total_revenue
    from gold.facts_table ft
    left join gold.dim_customers cu
    on ft.customer_key = cu.customer_key
    group by cu.customer_key, cu.first_name, cu.last_name
    order by total_revenue desc
    ```
    
    | **customer_key** | **first_name** | **last_name** | **total_revenue** |
    |------------------|----------------|---------------|--------------------|
    | 1302             | Nichole        | Nara          | 13294              |
    | 1133             | Kaitlyn        | Henderson     | 13294              |
    | 1309             | Margaret       | He            | 13268              |
    | 1132             | Randall        | Dominguez     | 13265              |
    | 1301             | Adriana        | Gonzalez      | 13242              |
    | 1322             | Rosa           | Hu            | 13215              |
    | 1125             | Brandi         | Gill          | 13195              |
    | 1308             | Brad           | She           | 13172              |
    | 1297             | Francisco      | Sara          | 13164              |
    | 434              | Maurice        | Shan          | 12914              |
    | ...              | ...            | ...           | ...                |


    ---


    18. What is the distribution of sold items across countries?
    ```sql
    select cu.country, sum(quantity) as total_sold_items
    from gold.facts_table ft
    left join gold.dim_customers cu
    on ft.customer_key = cu.customer_key
    group by cu.country
    ```

    | **country**        | **total_sold_items** |
    |--------------------|----------------------|
    | Australia          | 13346                |
    | Canada             | 7630                 |
    | France             | 5559                 |
    | Germany            | 5626                 |
    | N/A                | 871                  |
    | United Kingdom     | 6910                 |
    | United States      | 20481                |
    
    
    ---

    
    19. Which 5 products generate the highest revenue?
    ```sql
    select top 5 pr.product_name, sum(ft.sales_amount) as total_revenue
    from gold.facts_table ft
    left join gold.dim_products pr
    on ft.product_key = pr.product_key
    group by pr.product_name
    order by total_revenue desc
    ```
    
    | **product_name**             | **total_revenue** |
    |-----------------------------|-------------------|
    | Mountain-200 Black- 46      | 1373454           |
    | Mountain-200 Black- 42      | 1363128           |
    | Mountain-200 Silver- 38     | 1339394           |
    | Mountain-200 Silver- 46     | 1301029           |
    | Mountain-200 Black- 38      | 1294854           |
    
    
    ---
    
    
    20. What are the 5 worst-performing products by sale?
    ```sql
    select top 5 pr.product_name, sum(ft.sales_amount) as total_revenue
    from gold.facts_table ft
    left join gold.dim_products pr
    on ft.product_key = pr.product_key
    group by pr.product_name
    order by total_revenue asc
    ```

    | **product_name**          | **total_revenue** |
    |---------------------------|-------------------|
    | Racing Socks- L           | 2430              |
    | Racing Socks- M           | 2682              |
    | Patch Kit/8 Patches       | 6382              |
    | Bike Wash - Dissolver     | 7272              |
    | Touring Tire Tube         | 7440              |
    
    
    ---


    21. Which 5 subcategories generate the highest revenue?
    ```sql
    select top 5 pr.subcateegory, sum(ft.sales_amount) as total_revenue
    from gold.facts_table ft
    left join gold.dim_products pr
    on ft.product_key = pr.product_key
    group by pr.subcateegory
    order by total_revenue desc
    ```
    
    | **subcategory**   | **total_revenue** |
    |-------------------|-------------------|
    | Road Bikes        | 14519438          |
    | Mountain Bikes    | 9952254           |
    | Touring Bikes     | 3844580           |
    | Tires and Tubes   | 244634            |
    | Helmets           | 225435            |


    ---
    
    
    22. Find top 10 customers who have generated highest sales
    ```sql 
    select top 10 cu.customer_key, cu.first_name, cu.last_name, sum(sales_amount) as total_sales
    from gold.facts_table ft
    left join gold.dim_customers cu
    on ft.customer_key = cu.customer_key
    group by cu.customer_key, cu.first_name, cu.last_name
    order by total_sales desc
    ```
        
    | **customer_key** | **first_name** | **last_name** | **total_sales** |
    |------------------|----------------|---------------|-----------------|
    | 1302             | Nichole        | Nara          | 13294           |
    | 1133             | Kaitlyn        | Henderson     | 13294           |
    | 1309             | Margaret       | He            | 13268           |
    | 1132             | Randall        | Dominguez     | 13265           |
    | 1301             | Adriana        | Gonzalez      | 13242           |
    | 1322             | Rosa           | Hu            | 13215           |
    | 1125             | Brandi         | Gill          | 13195           |
    | 1308             | Brad           | She           | 13172           |
    | 1297             | Francisco      | Sara          | 13164           |
    | 434              | Maurice        | Shan          | 12914           |


    ---


    23. Find the bottom 3 customers with fewest orders placed
    ```sql 
    select top 3 cu.customer_key, cu.first_name, cu.last_name, count(order_number) as total_orders
    from gold.facts_table ft
    left join gold.dim_customers cu
    on ft.customer_key = cu.customer_key
    group by cu.customer_key, cu.first_name, cu.last_name
    order by total_orders asc
    ```

    | **customer_key** | **first_name** | **last_name** | **total_orders** |
    |------------------|----------------|---------------|------------------|
    | 14411            | Kaitlyn        | Ward          | 1                |
    | 13675            | Dylan          | Kumar         | 1                |
    | 18476            | Jared          | Ward          | 1                |



""")

        

    with subtab2:
        st.subheader("📈 Advanced Analysis")
        st.write("Deeper insights using complex SQL joins, aggregations, or trend analysis.")
        # You can plug in KPIs, grouped stats, trends, etc.