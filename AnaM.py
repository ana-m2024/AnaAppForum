import sqlite3
import pandas as pd

# Read the CSV file
df = pd.read_csv("Admission.csv")

# Create a SQLite database and connect to it
conn = sqlite3.connect("admission.db")

# Write the DataFrame to the database
df.to_sql("admission_data", conn, if_exists="replace")

# Close the database connection
conn.close()

import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("admission.db")

# Streamlit app
st.title("Graduate School Admissions")

# Function to execute SQL queries
def run_query(query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Sidebar with SQL query input
st.sidebar.header("SQL Playground")
user_query = st.sidebar.text_area("Enter your SQL query:")

if st.sidebar.button("Run Query"):
    if user_query:
        results = run_query(user_query)
        if results:
            st.write("Query Results:")
            st.write(results)
    else:
        st.warning("Please enter an SQL query.")

# Display the dataset using a default query
default_query = "SELECT * FROM admission_data LIMIT 10;"
default_results = run_query(default_query)

if default_results:
    st.write("Default Query Results:")
    st.write(default_results)

# Close the database connection when the app is done
conn.close()

if __name__ == "__main__":
    st.run()
