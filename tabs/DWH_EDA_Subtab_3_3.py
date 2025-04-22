import streamlit as st

def show():
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