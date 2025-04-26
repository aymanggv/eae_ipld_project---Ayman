import streamlit as st

def show():
    st.subheader("📈 Advanced Analysis")
    st.write("Deeper insights using complex SQL joins, aggregations, or trend analysis.")
        # You can plug in KPIs, grouped stats, trends, etc.
    st.markdown(
        """
        ---
        
        1. Change over time analysis
        ```sql
        select 
        year(order_date) as order_year, 
        month(order_date) as order_month,
        sum(sales_amount) as total_sales,
        count(distinct customer_key) as total_customers,
        sum(quantity) as total_quantity
        from gold.facts_table
        where order_date is not null
        group by year(order_date), month(order_date)
        order by year(order_date), month(order_date)
        
        -- Below is cleaner version of above code
        select 
        datetrunc(month, order_date) as order_date, 
        sum(sales_amount) as total_sales,
        count(distinct customer_key) as total_customers,
        sum(quantity) as total_quantity
        from gold.facts_table
        where order_date is not null
        group by datetrunc(month, order_date)
        order by datetrunc(month, order_date)

        -- Below is another version to get the month name instead of number
        select 
        format(order_date, 'yyyy-MMM') as order_date, 
        sum(sales_amount) as total_sales,
        count(distinct customer_key) as total_customers,
        sum(quantity) as total_quantity
        from gold.facts_table
        where order_date is not null
        group by format(order_date, 'yyyy-MMM')
        order by format(order_date, 'yyyy-MMM')

        ```
        | order_year | order_month | total_sales | total_customers | total_quantity |
        |------------|-------------|-------------|------------------|----------------|
        | 2010       | 12          | 43419       | 14               | 14             |
        | 2011       | 1           | 469795      | 144              | 144            |
        | 2011       | 2           | 466307      | 144              | 144            |
        | 2011       | 3           | 485165      | 150              | 150            |
        | 2011       | 4           | 502042      | 157              | 157            |
        | 2011       | 5           | 561647      | 174              | 174            |
        | 2011       | 6           | 737793      | 230              | 230            |
        | 2011       | 7           | 596710      | 188              | 188            |
        | 2011       | 8           | 614516      | 193              | 193            |
        | 2011       | 9           | 603047      | 185              | 185            |
        | ...       | ...           | ...      | ...              | ...            |
        
        ---
        2. Find change in customers over the months
        ```sql
        select 
        datetrunc(month, order_date) as order_date, 
        sum(sales_amount) as total_sales,
        count(distinct customer_key) as total_customers,
        count(distinct customer_key) - lag(count(distinct customer_key)) over(order by datetrunc(month, order_date)) as customer_changes,
        sum(quantity) as total_quantity
        from gold.facts_table
        where order_date is not null
        group by datetrunc(month, order_date)
        order by datetrunc(month, order_date)
        ```
        | order_date | total_sales | total_customers | customer_changes | total_quantity |
        |------------|-------------|------------------|------------------|----------------|
        | 2010-12-01 | 43419       | 14               | NULL             | 14             |
        | 2011-01-01 | 469795      | 144              | 130              | 144            |
        | 2011-02-01 | 466307      | 144              | 0                | 144            |
        | 2011-03-01 | 485165      | 150              | 6                | 150            |
        | 2011-04-01 | 502042      | 157              | 7                | 157            |
        | 2011-05-01 | 561647      | 174              | 17               | 174            |
        | 2011-06-01 | 737793      | 230              | 56               | 230            |
        | 2011-07-01 | 596710      | 188              | -42              | 188            |
        | 2011-08-01 | 614516      | 193              | 5                | 193            |
        | 2011-09-01 | 603047      | 185              | -8               | 185            |
        | ... | ...      | ...              | ...               | ...            |
        
        ---
        
        
        3. Calculate the total sales per month and the running total of sales over time
        ```sql
        select order_date,
        total_sales,
        sum (total_sales) over (order by order_date) as running_total_sales
        from(
        select 
        datetrunc(month, order_date) as order_date, 
        sum(sales_amount) as total_sales
        from gold.facts_table
        where order_date is not null
        group by datetrunc(month, order_date)
        ) t
        ```
        | order_date | total_sales | running_total_sales |
        |------------|-------------|---------------------|
        | 2010-12-01 | 43419       | 43419               |
        | 2011-01-01 | 469795      | 513214              |
        | 2011-02-01 | 466307      | 979521              |
        | 2011-03-01 | 485165      | 1464686             |
        | 2011-04-01 | 502042      | 1966728             |
        | 2011-05-01 | 561647      | 2528375             |
        | 2011-06-01 | 737793      | 3266168             |
        | 2011-07-01 | 596710      | 3862878             |
        | 2011-08-01 | 614516      | 4477394             |
        | 2011-09-01 | 603047      | 5080441             |
        | ... | ...      | ...             |
        
        
        ---
        
        
        4. Calculate the total sales per month and the running total of sales over time but reset it after the end of the year
        ```sql
        select order_date,
        total_sales,
        sum (total_sales) over (partition by datetrunc(year, order_date) order by order_date) as running_total_sales
        from(
        select 
        datetrunc(month, order_date) as order_date, 
        sum(sales_amount) as total_sales
        from gold.facts_table
        where order_date is not null
        group by datetrunc(month, order_date)
        ) t
        ```
        | order_date | total_sales | running_total_sales |
        |------------|-------------|---------------------|
        | 2010-12-01 | 43419       | 43419               |
        | 2011-01-01 | 469795      | 469795              |
        | 2011-02-01 | 466307      | 936102              |
        | 2011-03-01 | 485165      | 1421267             |
        | 2011-04-01 | 502042      | 1923309             |
        | 2011-05-01 | 561647      | 2484956             |
        | 2011-06-01 | 737793      | 3222749             |
        | 2011-07-01 | 596710      | 3819459             |
        | 2011-08-01 | 614516      | 4433975             |
        | 2011-09-01 | 603047      | 5037022             |
        | ... | ...      | ...             |

        
        ---
        
        5. Calculate the total sales per month, the running total of sales over time and movin average of the price
        
        ```sql
        select order_date,
        total_sales,
        sum (total_sales) over (order by order_date) as running_total_sales,
        avg(avg_price) over (order by order_date) as moving_average
        from(
        select 
        datetrunc(month, order_date) as order_date, 
        sum(sales_amount) as total_sales,
        avg (price) as avg_price
        from gold.facts_table
        where order_date is not null
        group by datetrunc(month, order_date)
        ) t
        ```
        
        | order_date | total_sales | running_total_sales | moving_average |
        |------------|-------------|---------------------|----------------|
        | 2010-12-01 | 43419       | 43419               | 3101           |
        | 2011-01-01 | 469795      | 513214              | 3181           |
        | 2011-02-01 | 466307      | 979521              | 3200           |
        | 2011-03-01 | 485165      | 1464686             | 3208           |
        | 2011-04-01 | 502042      | 1966728             | 3206           |
        | 2011-05-01 | 561647      | 2528375             | 3209           |
        | 2011-06-01 | 737793      | 3266168             | 3209           |
        | 2011-07-01 | 596710      | 3862878             | 3204           |
        | 2011-08-01 | 614516      | 4477394             | 3202           |
        | 2011-09-01 | 603047      | 5080441             | 3208           |
        | ... | ...      | ...             | ...           |

        
        ---
        
        6. Analyze the yearly performance of products by comparing each products sales to both its average sales performance and the previous years sales
        ```sql
        with cte as(
        select 
        year(f.order_date) as order_year,
        p.product_name,
        sum(f.sales_amount) as current_sales
        from gold.facts_table f
        left join gold.dim_products p
        on f.product_key = p.product_key
        where order_date is not null
        group by year(f.order_date), p.product_name
        )
        select order_year, 
        product_name, 
        current_sales, 
        AVG(current_sales) over(partition by product_name) as avg_sales, 
        current_sales - AVG(current_sales) over(partition by product_name) as diff_avg,
        case when current_sales - AVG(current_sales) over(partition by product_name) > 0 then 'Above Average'
            when current_sales - AVG(current_sales) over(partition by product_name) < 0 then 'Below Average'
            else 'Average'
        end as avg_change,
        LAG(current_sales) over (partition by product_name order by order_year) as previous_year_sales,
        current_sales - LAG(current_sales) over (partition by product_name order by order_year) as diff_yoy,
        case when current_sales - LAG(current_sales) over (partition by product_name order by order_year) > 0 then 'Increase'
            when current_sales - LAG(current_sales) over (partition by product_name order by order_year) < 0 then 'Decrease'
            else 'No Change'
        end as avg_change
        from cte
        order by product_name, order_year
        ;
        ```
        
        | order_year | product_name           | current_sales | avg_sales | diff_avg | avg_change     | previous_year_sales | diff_yoy | avg_change   |
        |------------|------------------------|----------------|-----------|-----------|----------------|----------------------|----------|--------------|
        | 2012       | All-Purpose Bike Stand | 159            | 13197     | -13038    | Below Average  | NULL                 | NULL     | No Change    |
        | 2013       | All-Purpose Bike Stand | 37683          | 13197     | 24486     | Above Average  | 159                  | 37524    | Increase     |
        | 2014       | All-Purpose Bike Stand | 1749           | 13197     | -11448    | Below Average  | 37683                | -35934   | Decrease     |
        | 2012       | AWC Logo Cap           | 72             | 6570      | -6498     | Below Average  | NULL                 | NULL     | No Change    |
        | 2013       | AWC Logo Cap           | 18891          | 6570      | 12321     | Above Average  | 72                   | 18819    | Increase     |
        | 2014       | AWC Logo Cap           | 747            | 6570      | -5823     | Below Average  | 18891                | -18144   | Decrease     |
        | 2013       | Bike Wash - Dissolver  | 6960           | 3636      | 3324      | Above Average  | NULL                 | NULL     | No Change    |
        | 2014       | Bike Wash - Dissolver  | 312            | 3636      | -3324     | Below Average  | 6960                 | -6648    | Decrease     |
        | 2013       | Classic Vest- L        | 11968          | 6240      | 5728      | Above Average  | NULL                 | NULL     | No Change    |
        | 2014       | Classic Vest- L        | 512            | 6240      | -5728     | Below Average  | 11968                | -11456   | Decrease     |
        | ...        | ...                    | ...            | ...       | ...       | ...            | ...                  | ...      | ...          |

        
        ---
        
        
        7. Which categories contribute the most to overall sales?
        ```sql
        with cte as
        (
        select 
        p.category,
        sum(f.sales_amount) as total_sales
        from gold.facts_table f
        left join gold.dim_products p
        on f.product_key = p.product_key
        where order_date is not null
        group by p.category
        )
        select *, 
        SUM(total_sales) over () as overall_sales,
        concat(round((cast (total_sales as float) * 100.0 / sum(total_sales) over ()), 2), '%') AS percent_of_total
        from cte
        order by total_sales desc
        ```
        
        | category    | total_sales | overall_sales | percent_of_total |
        |-------------|-------------|----------------|------------------|
        | Bikes       | 28311657    | 29351258       | 96.46%           |
        | Accessories | 699909      | 29351258       | 2.38%            |
        | Clothing    | 339692      | 29351258       | 1.16%            |
        
        
        ---
        
        
        8. -- Segment products into cost ranges and count how many segments fall into each categtory
        ```sql
        with cte as
        (SELECT
        product_key,
        product_name,
        cost,
        CASE WHEN cost < 100 THEN 'Below 100'
            WHEN cost BETWEEN 100 AND 500 THEN '100-500'
            WHEN cost BETWEEN 500 AND 1000 THEN ' 500-1000'
            ELSE 'Above 1000'
        END cost_range
        FROM gold.dim_products
        )
        SELECT
        cost_range,
        COUNT (product_key) AS total_products
        FROM cte
        GROUP BY cost_range
        ORDER BY total_products DESC
        ```
        
        | cost_range   | total_products |
        |--------------|----------------|
        | Below 100    | 110            |
        | 100-500      | 101            |
        | 500-1000     | 45             |
        | Above 1000   | 39             |


        ---

        
        9.  Group customers into three segments based on their spending behavior:  
            VIP: at least 12 months of history and spending more than €5,000.  
            Regular: at least 12 months of history but spending €5,000 or less.  
            New: lifespan less than 12 months.  
            And find the total number of customers by each group.

        ```sql
        with cte as (
        SELECT
        c.customer_key,
        sum(f.sales_amount) as total_spending,
        MIN(order_date) as first_order_date,
        MAX(order_date) as last_order_date,
        DATEDIFF(MONTH, MIN(order_date), MAX(order_date)) as lifespan, 
        case when sum(f.sales_amount) > 5000 and DATEDIFF(MONTH, MIN(order_date), MAX(order_date)) >= 12 then 'VIP'
            when sum(f.sales_amount) < 5000 and DATEDIFF(MONTH, MIN(order_date), MAX(order_date)) >= 12 then 'Regular'
            when DATEDIFF(MONTH, MIN(order_date), MAX(order_date)) <= 12 then 'New'
            else 'N/A'
        end as customer_segment
        FROM gold.facts_table f
        left join gold.dim_customers c
        on f.customer_key = c.customer_key
        group by c.customer_key
        )
        select
        customer_segment,
        count(*) as total_customers
        from cte
        group by customer_segment
        ```

        | customer_segment | total_customers |
        |------------------|-----------------|
        | N/A              | 2               |
        | New              | 14,629          |
        | Regular          | 2,198           |
        | VIP              | 1,655           |

        
        ---
        
        
        """
    )