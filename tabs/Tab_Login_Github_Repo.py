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
            <label class="folder" for="datasets">sql</label>
            <input type="checkbox" id="datasets"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/Login-Details-Data-Analysis/blob/main/sql/login_details_ddl.sql"> login_details_ddl.sql </a> <span class="comment"># Script to create database</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/Login-Details-Data-Analysis/blob/main/sql/login_details_data_analysis.sql"> login_details_data_analysis.sql </a> <span class="comment"># Script to analyze data</span></li>            
            </ul>
        </li>
            </ul>
        </li>
        <li class="file"> <a href="https://github.com/aymanggv/Login-Details-Data-Analysis/blob/main/LICENSE"> LICENSE </a> <span class="comment"># License</span></li>
        <li class="file"> <a href="https://github.com/aymanggv/Login-Details-Data-Analysis/blob/main/README.md"> README.md </a> <span class="comment"># Project overview</span></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
