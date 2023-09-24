# Core Pkgs
import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('Admission.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


admission = ['Serial Number,', 'GRE Score,', 'TOEFL Score,', 'University Rating,', 'Statement of Purpose,', 'Letter of Rec,', 'Undergraduate GPA,', 'Research,', 'Admission Chance']



def main():
	st.title("Graduate School Admissions")
	st.image('dogs2.jpg', width=10)
	

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("Type your SQL Code here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.expander("Table Info"):
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

