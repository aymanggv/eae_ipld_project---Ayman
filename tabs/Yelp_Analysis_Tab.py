import streamlit as st

def show():
    st.subheader("🔍 Data Analysis")
    st.write("Exploration of the Yelp dataset using SQL on Snowflake.")
    st.markdown("""
        ---
        1. Identify number of businesses for each category:
        ```sql
        with CTE as (
        select business_id, trim(A.value) as category 
        from tbl_yelp_businesses_cleaned,
        lateral split_to_table(business_categories, ',') A
        )
        select category, count(*) as number_of_businesses
        from CTE
        group by 1 --1 means first column
        order by number_of_businesses desc
        ```
        | CATEGORY         | NUMBER_OF_BUSINESSES |
        |------------------|----------------------|
        | Restaurants      | 52268                |
        | Food             | 27781                |
        | Shopping         | 24395                |
        | Home Services    | 14356                |
        | Beauty & Spas    | 14292                |
        | Nightlife        | 12281                |
        | Health & Medical | 11890                |
        | Local Services   | 11198                |
        | Bars             | 11065                |
        | Automotive       | 10773                |
        | ...       | ...                |
        
        ---
        
        2. Find date of first and last order and how many years of sales are there.
        ```sql
        with CTE as (
        select business_id, trim(A.value) as category 
        from tbl_yelp_businesses_cleaned,
        lateral split_to_table(business_categories, ',') A
        )
        select tbl_yelp_reviews_cleaned.user_id, count(distinct CTE.business_id) 
        from CTE
        Join tbl_yelp_reviews_cleaned 
        on CTE.business_id = tbl_yelp_reviews_cleaned.business_id
        where category = 'Restaurants'
        group by 1
        order by 2 desc
        limit 10
        ```
        
        | USER_ID                     | COUNT(DISTINCT CTE.BUSINESS_ID) |
        |------------------------------|---------------------------------|
        | -G7Zkl1wIWBBmD0KRy_sCw        | 1202                           |
        | _BcWyKQL16ndpBdggh2kNA        | 1166                           |
        | fr1Hz2acAb3OaL3l6DyKNg        | 1058                           |
        | 1HM81n6n4iPIFU5d2Lokhw        | 1009                           |
        | Xw7ZjaGfr0WNVt6s_5KZfA        | 926                            |
        | ET8n-r7glWYqZhuR6GcdNw        | 891                            |
        | pou3BbKsIozfH50rxmnMew        | 849                            |
        | VL12EhEdT4OWqGq0nIqkzw        | 832                            |
        | wXdbkFZsfDR7utJvbWElyA        | 773                            |
        | ouODopBKF3AqfCkuQEnrDg        | 744                            |

        
        ---
        
        3. Identify most popular category of businesses based on reviews:
        ```sql
        with CTE as (
        select business_id, trim(A.value) as category 
        from tbl_yelp_businesses_cleaned,
        lateral split_to_table(business_categories, ',') A
        )
        select CTE.category, count(*) as number_of_reviews 
        from CTE
        Join tbl_yelp_reviews_cleaned 
        on CTE.business_id = tbl_yelp_reviews_cleaned.business_id
        group by 1
        order by 2 desc
        ```
        
        | CATEGORY                    | NUMBER_OF_REVIEWS |
        |------------------------------|-------------------|
        | Restaurants                  | 4724471           |
        | Food                         | 1813593           |
        | Nightlife                    | 1539757           |
        | Bars                         | 1455553           |
        | American (Traditional)       | 1011646           |
        | American (New)               | 984540            |
        | Breakfast & Brunch           | 867430            |
        | Sandwiches                   | 691864            |
        | Seafood                      | 620247            |
        | Event Planning & Services    | 609553            |
        | ...    | ...            |

        
        
        ---
        
        
        4. Identify the 3 most recent reviews for each business:
        ```sql
        with cte as (
        select row_number() over(partition by tr.business_id order by tr.review_date desc) as rn, 
            tr.business_id, tb.business_name, tr.review_date, tr.review_stars, tr.review_text
        from tbl_yelp_reviews_cleaned as tr
        inner join tbl_yelp_businesses_cleaned as tb
        on tr.business_id = tb.business_id
        )
        select *
        from cte
        where rn<=3
        ```
        
        | RN | USER_ID                  | BUSINESS_NAME                  | REVIEW_DATE | RATING | REVIEW_TEXT |
        |----|---------------------------|---------------------------------|-------------|--------|-------------|
        | 1  | Bb67pizhqVU57T74ZimSnw     | Blades Hair Design              | 2017-06-11  | 5      | Julie is awesome. She spends time to see what you like. I was one that just wanted to show up and get haircut and usually waited too long. I have learned you can't do that here. I now have appoints every 5 weeks. The parking is easy, they have cookies/coffee when you enter |
        | 2  | Bb67pizhqVU57T74ZimSnw     | Blades Hair Design              | 2015-08-22  | 5      | Jason did an awesome job on my hair. Super knowledgable, and I couldn't be happier with it!! I would definitely recommend him and this place!! |
        | 3  | Bb67pizhqVU57T74ZimSnw     | Blades Hair Design              | 2014-12-07  | 1      | Last year I bought a group on, and after calling several times and never receiving a call back my group on expired. A waste f 80 dollars. Was not happy. |
        | 1  | OHSXdTFepfAsEqXgz_xXGA     | Bank of America Financial Center| 2021-11-17  | 1      | If I could give them a zero I would! The worst bank, the worst costumer service, the worst hours, and the meanest employees I ever had to deal with! Never regret ending my business with them! In two simple words "stay away!" |
        | 2  | OHSXdTFepfAsEqXgz_xXGA     | Bank of America Financial Center| 2021-10-07  | 1      | I have never once had a good experience at this location Bank of America on Campbell has continued to be the biggest letdown and disappointment that I've ever had while banking with Bank of America in all my years... |
        | 3  | OHSXdTFepfAsEqXgz_xXGA     | Bank of America Financial Center| 2021-02-06  | 1      | Bank of the America we fear our country could become. This is as shady as a check cashing place in the back of a liquor store. The tellers are rude... The one star is because the exit was not blocked. |
        | 1  | Nj4LMv64tJ8G2pNZQyW1Xg     | The Habit Burger Grill          | 2021-07-19  | 2      | I feel compelled to have another review of this place. First experience was horrific, last experience was amazing. This one was...somewhere less than great and only slightly better than meh. (full review) |
        | 2  | Nj4LMv64tJ8G2pNZQyW1Xg     | The Habit Burger Grill          | 2021-05-09  | 4      | Last visit was great. Lettuce wrap was awesome, fries were hot. Only reason not a 5 is because the young man didn't listen beyond lettuce wrap and fries. (full review) |
        | 3  | Nj4LMv64tJ8G2pNZQyW1Xg     | The Habit Burger Grill          | 2020-11-09  | 4      | The char burger with everything on it is pretty good. Not the best habit burger I've had but it was still a good burger. (full review) |
        | ...  | ...     | ...     | ...  | ...      | ... |


        
        
        ---
        
        
        5. Identify the months with the highest number of reviews:
        ```sql
        select month(review_date) as review_month, count(*) as number_of_reviews
        from tbl_yelp_reviews_cleaned
        group by 1
        order by 2 desc
        ```
        
        | REVIEW_MONTH | NUMBER_OF_REVIEWS |
        |--------------|-------------------|
        | 7            | 654627             |
        | 8            | 636384             |
        | 1            | 604532             |
        | 6            | 601737             |
        | 3            | 598555             |
        | 5            | 586575             |
        | 10           | 571809             |
        | 9            | 565374             |
        | 4            | 551471             |
        | 2            | 544125             |
        | 12           | 543573             |
        | 11           | 531518             |

        
        
        ---
        
        
        6. Find the percentage of 5 star reviews for each business:
        ```sql
        select tb.business_id, tb.business_name, count(*) as total_reviews, 
            count(case when tr.review_stars = '5' then 1 else null end) as five_star_reviews, 
            div0(five_star_reviews, total_reviews) * 100 as five_star_percentage
        from tbl_yelp_reviews_cleaned as tr
        inner join tbl_yelp_businesses_cleaned as tb
        on tr.business_id = tb.business_id
        group by 1, 2
        ```
        
        | BUSINESS_ID              | BUSINESS_NAME                         | TOTAL_REVIEWS | FIVE_STAR_REVIEWS | FIVE_STAR_PERCENTAGE |
        |---------------------------|---------------------------------------|---------------|------------------|--------------------------|
        | YaEwp8emNzySe-d0MKVbOw     | Midori Japanese Korean Restaurant    | 155           | 87               | 56.129000                |
        | JtxSBP-e3BKIdlefKUgFGg     | Edo Japan                            | 5             | 3                | 60.000000                |
        | o_9hBDxSVk0urSG9DhSF8A     | Airport Motors                       | 64            | 49               | 76.562500                |
        | 8E2--KcyOrJx8my51jid2w     | Jet City Espresso -Seminole Heights  | 221           | 167              | 75.565600                |
        | DkePId_VZgMx7skQ7aqMGw     | Z E N Thai & Japanese Cuisine        | 233           | 114              | 48.927000                |
        | KDALtmM8fy4dgpGjw5SzuA     | Andy Nails                           | 96            | 52               | 54.166700                |
        | iZNR8-rqsBL2afDk4Zxe8A     | Koch's Deli                          | 269           | 124              | 46.096700                |
        | 5YkucjpFYEhg4gsWU4B1hQ     | Little Pete's Restaurant             | 330           | 82               | 24.848500                |
        | nWEptpkm0YuZCBdnz3iSAQ     | Sonny's BBQ                          | 59            | 10               | 16.949200                |
        | u7uFQCoHFtBKCtbWUm6yZw     | Emeril's                             | 1635          | 842              | 51.498500                |
        | ...     | ...                             | ...          | ...              | ...                |


        ---


        7. Identify the top 5 most reviewed businesses in each city:
        ```sql
        with cte as(
            select tb.city, tb.business_id, tb.business_name, count(*) as total_reviews 
            from tbl_yelp_reviews_cleaned as tr
            inner join tbl_yelp_businesses_cleaned as tb
            on tr.business_id = tb.business_id
            group by 1, 2, 3
        )
        select *
        from cte
        qualify row_number() over(partition by city order by total_reviews desc) <=5
        ```
        
        | CITY           | BUSINESS_ID                    | BUSINESS_NAME                                 | TOTAL_REVIEWS |
        |----------------|---------------------------------|------------------------------------------------|-------------------|
        | Safety Hatbor  | tWTB736pFEFG3ICsrKpSxw           | Bay Area Fence Factory                        | 8                 |
        | Delaware County| s-A1_pxGRYL2x4gONVzvFA           | Easy Rider Repair                             | 13                |
        | Oldsmar        | c0F9yKr0bJuQDtG1lzDgmQ           | Craft Street Kitchen - Oldsmar                | 1059              |
        | Oldsmar        | O1Cw2yzf4bCuKjbVTljqUQ           | Flamestone American Grill                     | 549               |
        | Oldsmar        | kCV9CwW28Uz1ln4IXGhGwg           | Shaker & Peel                                 | 368               |
        | Oldsmar        | WZm72JqVRfpw2Pu3vag9gw           | Hot Tuna Sushi Bar & Grille                   | 335               |
        | Oldsmar        | FKgkGKRJYppEGCYuK_DOGg           | Salt Rock Tavern                              | 321               |
        | Philly         | YVYxF4XNzqm-XM_WbCNpnA           | Dizengoff                                     | 7                 |
        | Westville      | b74QZznVHAgdQBveV7Q0sw           | Speranza Wood-Fired Italian Kitchen           | 136               |
        | Westville      | SqR-SVD8otqLguw0rFUVvA           | La Tentacion Pizza & Mexican Grill            | 101               |
        | ...            | ...                             | ...                                            | ...               |

        
        
        ---
        
        
        8. Find the average rating of businesses that have at least 100 reviews:
        ```sql
        select tb.business_id, tb.business_name, count(*) as total_reviews, avg(review_stars) as avg_rating
        from tbl_yelp_reviews_cleaned as tr
        inner join tbl_yelp_businesses_cleaned as tb
        on tr.business_id = tb.business_id
        group by 1, 2
        having total_reviews >=100
        ```
        
        | BUSINESS_ID                      | BUSINESS_NAME                                             | TOTAL_REVIEWS | AVG_RATING |
        |-----------------------------------|-----------------------------------------------------------|-------------------|----------------|
        | d4GRmLdkPIsJBeOYE7fuqA            | Panera Bread                                               | 142               | 2.063380       |
        | BmKCJsV_payJ5ANqC7i85g            | The Vine Mediterranean Cafe and Market                    | 542               | 4.035055       |
        | QpAVPiH1Yujksd_ReL-x-g            | Inca's Peruvian Cuisine                                    | 309               | 4.119741       |
        | OWOOc0YjU_kioLeEgo5VCA            | Loveless Cafe                                              | 2480              | 4.293548       |
        | HzUJO2v5lUEIeYoOYsdWbw            | Russell's on Macklind                                      | 644               | 4.386646       |
        | sz5SMsTOTAshdfsaK98-TA            | Jane At The Marketplace                                    | 309               | 3.970874       |
        | NQ01WqVX0tojNHKn-0sFww            | Tir na nOg Irish Pub                                       | 251               | 3.266932       |
        | IYlUaKC9nICjiWdk-ShPlg            | Bub's Cafe                                                 | 177               | 3.887006       |
        | 7gtWQMLOEwCxh1I5j6uB4g            | St. James Cheese Company \| Warehouse District             | 313               | 4.485623       |
        | mhrW9O0O5hXGXGnEYBVoag            | Jacques-Imo's Cafe                                         | 2449              | 4.362189       |
        | ...                               | ...                                                       | ...               | ...            |

        
        
        ---
        

        9. Identify the top 10 users who have written the most reviews along with the businesses they reviewed:
        ```sql
        with cte as(
            select tr.user_id, count(*) as total_reviews
            from tbl_yelp_reviews_cleaned as tr
            group by 1
            order by 2 desc
            limit 10
        )
        select user_id, business_id
        from tbl_yelp_reviews_cleaned 
        where user_id in (select user_id from cte)
        group by 1, 2
        order by 1
        ```
        
        | USER_ID                        | BUSINESS_ID                     |
        |---------------------------------|----------------------------------|
        | -G7Zkl1wIWBBmD0KRy_sCw          | 7hwH3wiWB17U9Nw4EjJo0A           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | 3BgB3Pp0ZBzS3rwmXdw3nw           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | c_ZDp8DFUBLqCTZgD_m1iQ           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | 6kX0lZkpfQQmNWaIjpcsKw           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | 4iu7fFErsz7LS298z4bk8g           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | a_fp9I18WcbP86rQ4c_QZQ           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | VfqENB5K_bb3fg5-frm2dw           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | Quml7HOOuq1iaffy-UyhSQ           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | HNI6qvswn1KYybgJVqUWGg           |
        | -G7Zkl1wIWBBmD0KRy_sCw          | t6cQfzYnoJDWkYT60MENoA           |
        | ...                             | ...                              |


        ---

        

        10. Identify the top 10 businesses with the highest sentiment reviews:
        ```sql
        select tb.business_id, tb.business_name, count(*) as total_reviews
        from tbl_yelp_reviews_cleaned as tr 
        inner join tbl_yelp_businesses_cleaned as tb
        on tr.business_id = tb.business_id
        where sentiments = 'Positive'
        group by 1,2
        order by 3 desc
        limit 10
        ```
        
        | BUSINESS_ID                  | BUSINESS_NAME                          | TOTAL_REVIEWS |
        |------------------------------|-----------------------------------------|---------------|
        | _ab50qdWOk0DdB6XOrBitw        | Acme Oyster House                       | 7558          |
        | ac1AeYqs8Z4_e2X5M3if2A        | Oceana Grill                            | 7349          |
        | GXFMD0Z4jEVZBCsbPf4CTQ        | Hattie B’s Hot Chicken - Nashville      | 5972          |
        | ytynqOUb3hjKeJfRj5Tshw        | Reading Terminal Market                 | 5739          |
        | oBNrLz4EDhiscSlbOl8uAw        | Ruby Slipper - New Orleans              | 5148          |
        | iSRTaT9WngzB8JJ2YKJUig        | Mother's Restaurant                     | 4916          |
        | _C7QiQQc47AOEv4PE3Kong        | Commander's Palace                      | 4911          |
        | VQcCL9PiNL_wkGf-uF3fjg        | Royal House                             | 4883          |
        | GBTPC53ZrG1ZBY3DT8Mbcw        | Luke                                    | 4587          |
        | 6a4gLLFSgr-Q6CZXDLzBGQ        | Cochon                                  | 4410          |

    """)