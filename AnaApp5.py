import streamlit as st
import pandas as pd

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Admission2.db')
cursor = conn.cursor()

st.title("SQL Playground Graduate School")

def sql_executor(raw_code):
    conn.execute(raw_code)
    data = conn.fetchall()
    return data 


admission = ['Serial No.,', 'GRE Score,', 'TOEFL Score,', 'University Rating,', 'SOP,', 'LOR,', 'CGPA,', 'Research,', 'Admission Chance']



def main():
    st.title("Admission App")
    st.image('dogs2.jpg', width=100)

    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")

        # Columns/Layout
        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("Type your SQL Code Here")
                submit_code = st.form_submit_button("Execute")

            # Table of Info

            with st.expander("Table Information"):
                table_info = {'admission':admission}
                st.json(table_info)
            
        # Results Layouts
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                # Results 
                query_results = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)

                with st.expander("Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)


    else:
        st.subheader("About")





if __name__ == '__main__':
    main()

