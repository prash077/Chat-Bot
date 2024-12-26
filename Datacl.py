import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "db.sqlite3")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        if table_name != "sqlite_sequence":
            print(f"Clearing data from table: {table_name}")
            cursor.execute(f"DELETE FROM {table_name};")
            conn.commit()

    print("All data has been cleared from the database.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()
