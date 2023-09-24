import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Admission2.db')
c = conn.cursor()

st.title('SQL Playground')

# Sidebar for entering SQL query
query = st.sidebar.text_area('Enter your SQL query:')
execute_query = st.sidebar.button('Execute Query')

if execute_query:
    try:
        # Execute the SQL query
        c.execute(query)
        result = c.fetchall()

        # Display the result
        st.write("Query Result:")
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Close the database connection
conn.close()
