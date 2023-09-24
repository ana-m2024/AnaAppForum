%pip install pandas

import sqlite3
import pandas as pd

# CSV file path
csv_file = 'admission.csv'

# SQLite database file name
db_file = 'admission.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(db_file)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file)

# Replace spaces in column names with underscores
df.columns = df.columns.str.replace(' ', '_')

# Create an SQLite table using the DataFrame
df.to_sql('admission_data', conn, if_exists='replace', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f'CSV file "{csv_file}" has been successfully imported into the SQLite database "{db_file}" as a table "admission_data".')
