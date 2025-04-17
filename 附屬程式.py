import sqlite3
import pandas as pd # 為了更方便地顯示查詢結果

# Change the database filename to match the one used in the first code cell
db_filename = "teacher_research_areas_combined.db"
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# 查詢所有資料
cursor.execute("SELECT * FROM teachers")
results = cursor.fetchall()
print("所有資料：", results)

# 使用 pandas DataFrame 顯示資料
df = pd.read_sql_query("SELECT * FROM teachers", conn)
print("\n使用 Pandas DataFrame 顯示資料：")
print(df)

conn.close()
