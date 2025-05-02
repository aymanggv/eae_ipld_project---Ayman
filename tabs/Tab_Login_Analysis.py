import streamlit as st

def show():
    st.subheader("🔍 Data Analysis")
    st.write("Exploration of the login details dataset using SQL on MySQL Workbench.")
    st.markdown("""
        ---
        
        1. Management wants to see all users that did not login in the past 14 months. List those users. 
        ```sql
        select user_id, MAX(login_timestamp) as last_login_timestamp, DATE_ADD(CURDATE(), INTERVAL -14 MONTH) as current_month
        from logins
        group by user_id
        having last_login_timestamp < current_month
        ;
        ```
        
        | user_id | login_timestamp       | session_id | session_score |
        |--------|------------------------|------------|---------------|
        | '1'    | '2023-07-15 09:30:00'   | '1001'     | '85'          |
        | '2'    | '2023-07-22 10:00:00'   | '1002'     | '90'          |
        | '3'    | '2023-08-10 11:15:00'   | '1003'     | '75'          |
        | '4'    | '2023-08-20 14:00:00'   | '1004'     | '88'          |
        | '5'    | '2023-09-05 16:45:00'   | '1005'     | '82'          |
        | '6'    | '2023-10-12 08:30:00'   | '1006'     | '77'          |
        | '7'    | '2023-11-18 09:00:00'   | '1007'     | '81'          |
        | '8'    | '2023-12-01 10:30:00'   | '1008'     | '84'          |
        | '9'    | '2023-12-15 13:15:00'   | '1009'     | '79'          |
        | '10'   | '2024-06-25 15:00:00'   | '1010'     | '92'          |
        | ...    | ...                    | ...        | ...           |

        
        ---
        
        2. For the business units' quarterly analysis, calculate how many users and how many sessions were at each quarter.  
        -- Order by quarter from newest to oldest.  
        -- Return: first day of the quarter, user_cnt, session_cnt.

        ```sql
        with cte as (select COUNT(DISTINCT user_id) as users_count, count(*) as session_count ,quarter(Login_timestamp) as quarter_number
        from logins
        group by quarter(Login_timestamp)
        order by quarter_number
        )
        select cte.quarter_number, min(LOGIN_TIMESTAMP) as first_day_of_quarter, cte.session_count , cte.users_count
        from logins
        inner join cte
        on cte.quarter_number = quarter(logins.Login_timestamp)
        group by cte.quarter_number
        order by cte.quarter_number;

        /*Another solution below*/

        /*select DATETRUNC(quarter, ,MIN(LOGIN_TIMESTAMP) ) as first_quater_date
        COUNT (*) as session_cnt
        COUNT (distinct USER_ID) as user_cnt
        from logins
        group by DATEPART(quarter, LOGIN_TIMESTAMP)
        */
        ```
        
        | quarter_number | first_day_of_quarter     | session_count | users_count |
        |----------------|---------------------------|---------------|-------------|
        | '1'            | '2024-01-10 07:45:00'     | '8'           | '5'         |
        | '2'            | '2024-04-12 08:00:00'     | '8'           | '5'         |
        | '3'            | '2023-07-15 09:30:00'     | '5'           | '5'         |
        | '4'            | '2023-10-12 08:30:00'     | '7'           | '6'         |
        
        ---
        
        
        3. Display the user id's that Log-in in January 2024 and did not Log-in on November 2023.
        ```sql
        select distinct user_id
        from logins
        where LOGIN_TIMESTAMP like '2024-01%' 
        -- Jan users = 1,2,3,5
        -- Nov users = 2,4,6,7
        and user_id not in (
        select user_id 
        from logins
        where LOGIN_TIMESTAMP like '2023-11%'
        )
        ;

        /* Another solution below 
        select distinct(user_id)
        from logins
        where LOGIN_TIMESTAMP between '2024-01-01' and '2024-01-31'
        and USER_ID not in (select user_id
        from logins
        where LOGIN_TIMESTAMP between '2023-11-01' and '2023-11-30')
        ;*/
        ```
        
        | user_id |
        |---------|
        | '1'     |
        | '3'     |
        | '5'     |

        
        
        ---
        
        
        4. Add the percentage change in sessions from last quarter to query 2.  
        -- Return: first day of the quarter, session_cnt, session_cnt_prev, Session_percent_change.  
        -- Check video as he has diff answer. His quarter date starts from july and mine from Jan. Dont know if he intended that

        ```sql
        with cte as (select COUNT(DISTINCT user_id) as users_count, count(*) as session_count ,quarter(Login_timestamp) as quarter_number
        from logins
        group by quarter(Login_timestamp)
        order by quarter_number
        ),
        nest_cte as (
        select cte.quarter_number, min(LOGIN_TIMESTAMP) as first_day_of_quarter, cte.session_count , cte.users_count
        from logins
        inner join cte
        on cte.quarter_number = quarter(logins.Login_timestamp)
        group by cte.quarter_number
        order by cte.quarter_number)
        select *, lag(session_count, 1) over(order by quarter_number) as prev_session_count, 
        (session_count - (lag(session_count, 1) over(order by quarter_number))) / lag(session_count, 1) over(order by quarter_number)* 100 as session_percent_change 
        from nest_cte
        ;        
        ```
        
        | quarter_number | first_day_of_quarter     | session_count | users_count | prev_session_count | session_percent_change |
        |----------------|--------------------------|---------------|-------------|---------------------|------------------------|
        | '1'            | '2024-01-10 07:45:00'    | '8'           | '5'         | NULL                | NULL                   |
        | '2'            | '2024-04-12 08:00:00'    | '8'           | '5'         | '8'                 | '0.0000'               |
        | '3'            | '2023-07-15 09:30:00'    | '5'           | '5'         | '8'                 | '-37.5000'             |
        | '4'            | '2023-10-12 08:30:00'    | '7'           | '6'         | '5'                 | '40.0000'              |
        
        
        ---
        
        
        5. Display the users that had highest session score for each day.  
        -- Return date, usernme, score
        ```sql
        with cte as (select LOGIN_TIMESTAMP, max(SESSION_SCORE) as max_session_score
        from logins
        group by LOGIN_TIMESTAMP
        )
        select distinct(c.LOGIN_TIMESTAMP), c.max_session_score, l.USER_ID
        from cte c
        inner join logins l
        on c.LOGIN_TIMESTAMP = l.LOGIN_TIMESTAMP
        order by LOGIN_TIMESTAMP;
        
        /* Below is another version but need to verify with above
        with cte as (
        select USER_ID, CAST(LOGIN_TIMESTAMP AS DATE) AS login_date, SUM(session_score) as score
        from logins
        group by USER_ID, CAST(LOGIN_TIMESTAMP AS DATE)
        -- order by CAST(1ogin_timestamp as date), ,score
        )
        select * from (
        select *, ROW_NUMBER() over(partition by login_date order by score desc) as rn
        from cte
        ) a 
        where rn = 1;
        */
        ```
        
        | LOGIN_TIMESTAMP      | max_session_score | USER_ID |
        |----------------------|-------------------|---------|
        | '2023-07-15 09:30:00' | '85'              | '1'     |
        | '2023-07-22 10:00:00' | '90'              | '2'     |
        | '2023-08-10 11:15:00' | '75'              | '3'     |
        | '2023-08-20 14:00:00' | '88'              | '4'     |
        | '2023-09-05 16:45:00' | '82'              | '5'     |
        | '2023-10-12 08:30:00' | '77'              | '6'     |
        | '2023-11-10 07:45:00' | '82'              | '2'     |
        | '2023-11-15 11:00:00' | '80'              | '6'     |
        | '2023-11-18 09:00:00' | '81'              | '7'     |
        | '2023-11-25 09:30:00' | '84'              | '4'     |
        | ... | ...              | ...    |

        
        
        ---
        
        
        6. To identify our best users, return the users that had a session on every single day since their first login.
        -- Make assumptions if needed.
        -- Return: User_id

        ```sql
        /* Below diff from video as I do not have data that is up to date. I could add rows to see if below works.
        SELECT 
        USER_ID, 
        MIN(DATE(LOGIN_TIMESTAMP)) AS first_login,
        DATEDIFF(CURDATE(), MIN(DATE(LOGIN_TIMESTAMP))) + 1 AS no_of_login_days_required,
        COUNT(DISTINCT DATE(LOGIN_TIMESTAMP)) AS no_of_login_days
        FROM logins
        GROUP BY USER_ID
        HAVING no_of_login_days = no_of_login_days_required
        ORDER BY USER_ID;*/
        ;
        ```

        
        | LOGIN_TIMESTAMP      | max_session_score | USER_ID |
        |----------------------|-------------------|---------|
        | '2023-07-15 09:30:00' | '85'              | '1'     |
        | '2023-07-22 10:00:00' | '90'              | '2'     |
        | '2023-08-10 11:15:00' | '75'              | '3'     |
        | '2023-08-20 14:00:00' | '88'              | '4'     |
        | '2023-09-05 16:45:00' | '82'              | '5'     |
        | '2023-10-12 08:30:00' | '77'              | '6'     |
        | '2023-11-10 07:45:00' | '82'              | '2'     |
        | '2023-11-15 11:00:00' | '80'              | '6'     |
        | '2023-11-18 09:00:00' | '81'              | '7'     |
        | '2023-11-25 09:30:00' | '84'              | '4'     |


        ---


        7. -- On what days were there no logins at all?
        ```sql
        WITH RECURSIVE cte AS (
        SELECT MIN(DATE(LOGIN_TIMESTAMP)) AS first_date, DATE(CURDATE()) AS last_date
        FROM logins
        UNION ALL
        SELECT DATE_ADD(first_date, INTERVAL 1 DAY), last_date
        FROM cte
        WHERE first_date < last_date
        )
        SELECT * 
        FROM cte
        where first_date not in
        (select distinct date(login_timestamp) from logins
        )
        ```
        
        | first_date     | last_date     |
        |----------------|---------------|
        | '2023-07-16'   | '2025-04-27'  |
        | '2023-07-17'   | '2025-04-27'  |
        | '2023-07-18'   | '2025-04-27'  |
        | '2023-07-19'   | '2025-04-27'  |
        | '2023-07-20'   | '2025-04-27'  |
        | '2023-07-21'   | '2025-04-27'  |
        | '2023-07-23'   | '2025-04-27'  |
        | '2023-07-24'   | '2025-04-27'  |
        | '2023-07-25'   | '2025-04-27'  |
        | '2023-07-26'   | '2025-04-27'  |
        | ...            | ...           |


    """)