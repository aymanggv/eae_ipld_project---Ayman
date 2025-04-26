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
            <label class="folder" for="datasets">scripts</label>
            <input type="checkbox" id="datasets"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/Yelp-Data-Analysis/blob/main/scripts/Split_File.py"> Split_File.py </a> <span class="comment"># Python script</span></li>
            </ul>
        </li>
        <li>
            <label class="folder" for="docs">sql</label>
            <input type="checkbox" id="docs"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/Yelp-Data-Analysis/blob/main/sql/yelp_analytics"> yelp_analytics </a> <span class="comment"># Analytics SQLfile</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/Yelp-Data-Analysis/blob/main/sql/yelp_businesses%20table"> yelp_businesses table </a> <span class="comment"># Businesses DDL</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/Yelp-Data-Analysis/blob/main/sql/yelp_reviews_table"> yelp_reviews_table </a> <span class="comment"># Reviews DDL</span></li>            
            </ul>
        </li>
            </ul>
        </li>
        <li class="file"> <a href="https://github.com/aymanggv/Yelp-Data-Analysis/blob/main/End%20to%20End%20Flow%20-%20Yelp.png"> End to End Flow - Yelp.png </a> <span class="comment"># Data architecture</span></li>
        <li class="file"> <a href="https://github.com/aymanggv/Yelp-Data-Analysis/blob/main/README.md"> README.md </a> <span class="comment"># Project overview</span></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
