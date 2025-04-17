import sqlite3
import pandas as pd 

# Change the database filename to match the one used in the first code cell
db_filename = "teacher_research_areas_combined.db"
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

cursor.execute("SELECT * FROM teachers")
results = cursor.fetchall()
print("所有資料：", results)

df = pd.read_sql_query("SELECT * FROM teachers", conn)
print("\n使用 Pandas DataFrame 顯示資料：")
print(df)

conn.close()
