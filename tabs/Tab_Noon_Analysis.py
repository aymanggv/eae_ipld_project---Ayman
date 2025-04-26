import streamlit as st

def show():
    st.subheader("🔍 Data Analysis")
    st.write("Exploration of the Noon e-commerce dataset using SQL on MySQL Workbench.")
    st.markdown("""
        ---
        1. Find the top outlet by cuisine type without using limit and top function. 
        ```sql
        -- Below can be modified to list top 3 outlets
        with cte as(
        select Cuisine, Restaurant_id, count(*) as no_of_orders 
        from orders
        group by Cuisine, Restaurant_id
        )
        select * -- normal querying doesnt work so i have to subquery the main query to be able to use "where rn = 1" cuz that show sql works
        from (
        select *, row_number() over (partition by Cuisine order by no_of_orders desc) as rn
        from cte
        ) as a -- need to put an alias after every subquery
        where rn = 1;
        ```
        
        | cuisine   | restaurant_id | no_of_orders | rn |
        |-----------|---------------|--------------|----|
        | American  | BURGER99       | 8            | 1  |
        | Italian   | PIZZA123       | 11           | 1  |
        | Japanese  | SUSHI456       | 6            | 1  |
        | Lebanese  | KMKMH6787      | 10           | 1  |
        | Mexican   | TACO789        | 7            | 1  |

        
        ---
        
        2. How many new customers is Noon acquiring daily since their launch data?

        ```sql
        with cte as (
        select Customer_code, cast(min(Placed_at) as date) as first_order_date
        from orders
        group by Customer_code
        )
        select first_order_date, count(*) as no_of_new_customers
        from cte
        group by first_order_date
        order by first_order_date
        ;
        ```
        
        | first_order_date | no_of_new_customers |
        |------------------|---------------------|
        | 2025-01-01        | 2                   |
        | 2025-01-02        | 1                   |
        | 2025-01-03        | 1                   |
        | 2025-01-04        | 1                   |
        | 2025-01-05        | 3                   |
        | 2025-01-06        | 1                   |
        | 2025-01-07        | 1                   |
        | 2025-01-08        | 1                   |
        | 2025-01-09        | 1                   |
        | 2025-01-10        | 3                   |
        | ...        | ...                   |

        
        ---
        
        
        3. List all the users who were acquired in Jan 2025 who only placed 1 order in Jan and did not place any other order since.
        ```sql
        WITH cte AS (
        SELECT Customer_code, MIN(Placed_at) AS first_order_date, MAX(Placed_at) as last_order_date, count(*) as count_of_orders
        FROM orders
        GROUP BY Customer_code
        )
        SELECT *
        FROM cte
        WHERE DATE(first_order_date) LIKE '2025-01%' and DATE(last_order_date) like '2025-01%' and count_of_orders < 2
        order by Customer_code
        ;

        /*Another solution below*/

        /*select Customer_code, count(*) as no_of_orders
        from orders
        where MONTH(placed_at)=1 and YEAR (placed_at)=2025
        and Customer_code not in (select distinct Customer_code
        from orders
        where not (MONTH(placed_at)=1 and YEAR (placed_at)=2025)
        )
        group by Customer_code
        having COUNT(*)=1
        order by Customer_code
        ;*/
        ```
        
        | order_id           | created_at           | updated_at           | order_count |
        |--------------------|-----------------------|-----------------------|-------------|
        | BCD7890123456ABC    | 2025-01-10 20:15:00    | 2025-01-10 20:15:00    | 1           |
        | DEF5678901234MNO    | 2025-01-28 18:30:00    | 2025-01-28 18:30:00    | 1           |
        | EFG1234567890DEF    | 2025-01-11 09:30:00    | 2025-01-11 09:30:00    | 1           |
        | FGH7890123456GHI    | 2025-01-20 20:45:00    | 2025-01-20 20:45:00    | 1           |
        | GHI3456789012MNO    | 2025-01-29 11:45:00    | 2025-01-29 11:45:00    | 1           |
        | GHI5678901234XYZ    | 2025-01-03 14:30:00    | 2025-01-03 14:30:00    | 1           |
        | HIJ9876543210DEF    | 2025-01-12 14:45:00    | 2025-01-12 14:45:00    | 1           |
        | IJK1234567890JKL    | 2025-01-21 09:15:00    | 2025-01-21 09:15:00    | 1           |
        | JAN_ONLY_ORDER1     | 2025-01-15 13:30:00    | 2025-01-15 13:30:00    | 1           |
        | JAN_ONLY_ORDER2     | 2025-01-20 18:45:00    | 2025-01-20 18:45:00    | 1           |
        | ...                | ...                   | ...                   | ...         |

        
        
        ---
        
        
        4. List all the customers who haven't placed an order in the last 7 days but were acquired one month ago who placed their first order on promo.
        ```sql
        with cte as
        (SELECT Customer_code, MIN(Placed_at) AS first_order_date, MAX(Placed_at) as last_order_date
        FROM orders
        GROUP BY Customer_code
        )
        select cte.*, orders.Promo_code_Name as first_order_promo 
        from cte
        inner join orders
        on cte.first_order_date = orders.Placed_at
        where Promo_code_Name is not null AND last_order_date < (current_date() - INTERVAL 14 DAY) AND first_order_date < (current_date() - INTERVAL 45 DAY)
        ;
        ```
        
        | order_id           | created_at           | updated_at           | coupon_used |
        |--------------------|-----------------------|-----------------------|-------------|
        | UFDDN1991918XUY1    | 2025-01-01 15:30:20    | 2025-03-28 11:30:00    | Tasty50     |
        | ABC1234567890XYZ    | 2025-01-01 08:45:00    | 2025-01-05 13:20:00    | NEWUSER     |
        | DEF9876543210XYZ    | 2025-01-02 09:15:00    | 2025-03-02 09:15:00    | FIRSTORDER  |
        | GHI5678901234XYZ    | 2025-01-03 14:30:00    | 2025-01-03 14:30:00    | NEWUSER     |
        | JKL3456789012XYZ    | 2025-01-04 12:00:00    | 2025-01-04 12:00:00    | FIRSTORDER  |
        | PQR1234567890ABC    | 2025-01-06 11:30:00    | 2025-01-06 11:30:00    | NEWUSER     |
        | VWX5678901234ABC    | 2025-01-08 18:00:00    | 2025-01-08 18:00:00    | FIRSTORDER  |
        | BCD7890123456ABC    | 2025-01-10 20:15:00    | 2025-01-10 20:15:00    | NEWUSER     |
        | HIJ9876543210DEF    | 2025-01-12 14:45:00    | 2025-01-12 14:45:00    | FIRSTORDER  |
        | QRS7890123456DEF    | 2025-01-15 19:00:00    | 2025-01-15 19:00:00    | NEWUSER     |
        | ...                | ...                   | ...                   | ...         |
        
        
        ---
        
        
        5. The growth team is plnning to create a trigger that will target customers after their every 3rd order with a personalized message. Create a query to find those customers.
        ```sql
        with cte as (select Customer_code, order_id, row_number() over (partition by Customer_code order by order_id) as rn
        from orders
        group by Customer_code, order_id
        order by order_id)
        select * from cte
        where rn % 3 = 0 -- add an "and current date = today" code as well so that the team only sees only recent ordes and not old orders.
        ;
        ```
        
        | customer_code         | order_id       | rn  |
        |------------------------|----------------|-----|
        | UFDDN1991918XUY1        | OF1900191803    | 3   |
        | THIRD_ORDER_CUST1       | OF1900191847    | 3   |
        | THIRD_ORDER_CUST2       | OF1900191850    | 3   |
        | MULTI_CUISINE_CUST      | OF1900191853    | 3   |
        | PROMO_FIRST_ONLY        | OF1900191861    | 3   |
        | LAST_ORDER_7DAYS        | OF1900191864    | 3   |
        | ABC9876543210MNO        | OF1900191867    | 3   |
        | MULTI_CUISINE_CUST      | OF1900191870    | 6   |
        | UVW7890123456JKL        | OF1900191873    | 3   |

        
        
        ---
        
        
        6. List all the customers who placed more than 1 order and all their orders were placed using a promo only.
        ```sql
        select Customer_code, count(*) as no_of_orders, count(Promo_code_Name) as promo_code_orders
        from orders
        group by Customer_code
        having no_of_orders > 1 and no_of_orders = promo_code_orders
        ;
        ```
        
        | customer_code        | no_of_orders | promo_code_orders |
        |-----------------------|--------------|-------------------|
        | DEF9876543210XYZ       | 2            | 2                 |
        | UVW7890123456JKL       | 4            | 4                 |


        ---


        7. What percent of customers were organically acquired in Jan 2025? (Placed their first order without using a promo code)
        ```sql
        with cte as (SELECT Customer_code, MIN(Placed_at) AS first_order_date
        FROM orders
        where Month(Placed_at) = 1
        group by Customer_code
        )
        select count(case when Promo_code_Name is null then orders.Customer_code end) / count(distinct orders.Customer_code) * 100.0
        from cte
        inner join orders 
        on cte.first_order_date = orders.Placed_at
        ;

        /*Another solution below*/

        /*with cte as (
        select *, ROW_NUMBER() over (partition by customer_code order by placed_at) as rn
        from orders
        where MONTH (placed_at)=1
        )
        select count(case when rn=1 and Promo_code_Name is null then Customer_code end)
        *100/ COUNT(distinct Customer_code)
        from cte*/        
        ```
        
        | percentage_customers_without_promo |
        |-------------------------------------|
        | 43.90244                            |

    """)