# Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('Admission2.db')
c = conn.cursor()

# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


admission_data = ['Serial No.,', 'GRE Score,', 'TOEFL Score,', 'University Rating,', 'SOP,', 'LOR,', 'CGPA,', 'Research,', 'Admission Chance']



def main():
	st.title("SQL Playground Graduate School Admission")
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
				table_info = {'admission_data':admission_data}
				st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("SQL Query Executed")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
		st.subheader("Info")





if __name__ == '__main__':
	main()

