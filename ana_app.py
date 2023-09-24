import streamlit as st
import pandas as pd
import numpy as np

# Streamlit app
st.title('SQL Playground')

# Text input for SQL queries
sql_query = st.text_area('Enter your SQL query:')



# Execute SQL query when the button is pressed
if st.button('Run Query'):
    try:
        conn = sqlite3.connect('admission.db')
        cursor = conn.cursor()

        cursor.execute(sql_query)
        results = cursor.fetchall()

        if results:
            # Display results as a DataFrame
            st.dataframe(pd.DataFrame(results))
        else:
            st.write('No results to display.')

    except Exception as e:
        st.error(f'An error occurred: {str(e)}')

    finally:
        conn.close()