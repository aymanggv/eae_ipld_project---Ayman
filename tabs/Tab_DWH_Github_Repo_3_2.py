import streamlit as st

def show():
    st.header("📂 GitHub Repository")
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)

    st.markdown("""
        <style>
        .tree ul {
        list-style-type: none;
        font-family: monospace;
        padding-left: 1em;
        line-height: 1.6;
        }
        .tree input {
        display: none;
        }
        .tree label {
        cursor: pointer;
        }
        .tree input:checked + ul {
        display: block;
        }
        .tree ul ul {
        display: none;
        }
        .folder::before {
        content: "📁 ";
        }
        .file::before {
        content: "📄 ";
        }
        .comment {
        color: gray;
        font-size: 0.85em;
        font-style: italic;
        margin-left: 4px;
        }
        </style>

        <div class="tree">
        <ul>
        <li>
            <label class="folder" for="data_analysis">data_analysis</label>
            <input type="checkbox" id="data_analysis"/>
            <ul>
            <li>
                <label class="folder" for="exploratory">exploratory_data_analysis</label>
                <input type="checkbox" id="exploratory"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/data_analysis/exploratory_data_analysis/dwh_exploratory_data_analysis.sql"> dwh_exploratory_data_analysis.sql </a> <span class="comment"># SQL script for EDA</span></li>
                </ul>
            </li>
            <li>
                <label class="folder" for="advanced">advanced_data_analysis</label>
                <input type="checkbox" id="advanced"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/data_analysis/advanced_data_analysis/dwh_advanced_analytics.sql"> dwh_advanced_analytics.sql </a> <span class="comment"># SQL script for advanced analysis</span></li>
                </ul>
            </li>
            <li>
                <label class="folder" for="reports">reports</label>
                <input type="checkbox" id="reports"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/data_analysis/reports/report_customer.sql"> report_customer.sql </a> <span class="comment"># SQL script for customer report</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/data_analysis/reports/report_product.sql"> report_product.sql </a> <span class="comment"># SQL script for product report</span></li>                
                </ul>
            </li>
            </ul>
        </li>

        <li>
            <label class="folder" for="datasets">datasets</label>
            <input type="checkbox" id="datasets"/>
            <ul>
            <li>
                <label class="folder" for="crm">source_crm</label>
                <input type="checkbox" id="crm"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/datasets/source_crm/cust_info.csv"> cust_info.csv </a> <span class="comment"># Customer data</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/datasets/source_crm/cust_info.csv"> prd_info.csv </a> <span class="comment"># Product data</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/datasets/source_crm/cust_info.csv"> sales_details.csv </a> <span class="comment"># Sales data</span></li>
                </ul>
            </li>
            <li>
                <label class="folder" for="erp">source_erp</label>
                <input type="checkbox" id="erp"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/datasets/source_erp/CUST_AZ12.csv"> CUST_AZ12.csv </a> <span class="comment"># Customer birthdate data</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/datasets/source_erp/LOC_A101.csv"> LOC_A101.csv </a> <span class="comment"># Customer location data</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/datasets/source_erp/PX_CAT_G1V2.csv"> PX_CAT_G1V2.csv </a> <span class="comment"># Product categories and sub-categories data</span></li>
                </ul>
            </li>
            </ul>
        </li>
        <li>
            <label class="folder" for="docs">docs</label>
            <input type="checkbox" id="docs"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/ETL.png"> ETL.png </a> <span class="comment"># ETL techniques</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/data_architecture.png"> data_architecture.png </a> <span class="comment"># Architecture</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/data_catalog.md"> data_catalog.md </a> <span class="comment"># Field descriptions</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/data_flow.png"> data_flow.png </a> <span class="comment"># Data flow</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/data_integration.png"> data_integration.png </a> <span class="comment"># Data itegration</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/data_layers.pdf"> data_layers.pdf </a> <span class="comment"># Data layers</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/data_model.png"> data_model.png </a> <span class="comment"># Star schema</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/docs/naming_conventions.md"> naming_conventions.md </a><span class="comment"># Naming guidelines</span></li>
            </ul>
        </li>

        <li>
            <label class="folder" for="scripts">scripts</label>
            <input type="checkbox" id="scripts"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/create_dwh_and_schemas.sql"> create_dwh_and_schemas.sql </a> <span class="comment"># Create the DWH</span></li>
            <li>
                <label class="folder" for="bronze">bronze</label>
                <input type="checkbox" id="bronze"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/bronze/create_ddl_bronze.sql"> create_ddl_bronze.sql </a> <span class="comment"># Bronze DDL</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/bronze/loading_data_bronze.sql"> loading_data_bronze.sql </a> <span class="comment"># Loading data into the bronze layer</span></li>                
                </ul>
            </li>
            <li>
                <label class="folder" for="silver">silver</label>
                <input type="checkbox" id="silver"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/silver/create_ddl_silver.sql"> create_ddl_silver.sql </a> <span class="comment"># Silver DDL</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/silver/loading_data_silver.sql"> stored_procedure_loading_data_silver.sql </a> <span class="comment"># Loading data into the silver layer</span></li>                
                </ul>
            </li>
            <li>
                <label class="folder" for="gold">gold</label>
                <input type="checkbox" id="gold"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/gold/create_gold.dim_customers.sql"> create_gold.dim_customers.sql </a> <span class="comment"># Customer dimension</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/gold/create_gold.dim_products.sql"> create_gold.dim_products.sql </a> <span class="comment"># Products dimension</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/scripts/gold/create_gold.facts_table.sql"> create_gold.facts_table.sql </a> <span class="comment"># Sales fact table</span></li>      
                </ul>
            </li>
            </ul>
        </li>

        <li>
            <label class="folder" for="tests">tests</label>
            <input type="checkbox" id="tests"/>
            <ul>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/tests/data_cleaning_silver.crm_cust_info.sql"> data_cleaning_silver.crm_cust_info.sql </a> <span class="comment"># Cleaning silver.crm_cust_info.sql</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/tests/data_cleaning_silver.crm_prd_info.sql"> data_cleaning_silver.crm_prd_info.sql </a> <span class="comment"># Cleaning silver.prd_info.sql</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/tests/data_cleaning_silver.crm_sales_details.sql"> data_cleaning_silver.crm_sales_details.sql </a> <span class="comment"># Cleaning silver.sales_details.sql</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/tests/data_cleaning_silver.erp_cust_az12.sql"> data_cleaning_silver.erp_cust_az12.sql </a> <span class="comment"># Cleaning silver.erp_cust_az12.sql</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/tests/data_cleaning_silver.erp_loc_101.sql"> data_cleaning_silver.erp_loc_101.sql </a> <span class="comment"># Cleaning silver.erp_loc_101.sql</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/tests/data_cleaning_silver.erp_px_cat_g1v2.sql"> data_cleaning_silver.erp_px_cat_g1v2.sql </a> <span class="comment"># Cleaning silver.erp_px_cat_g1v2.sql</span></li>
            </ul>
        </li>

        <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/LICENSE"> LICENSE </a> <span class="comment"># License info</span></li>
        <li class="file"> <a href="https://github.com/aymanggv/data-warehouse-project/blob/main/README.md"> README.md </a> <span class="comment"># Project overview</span></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
