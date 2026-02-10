import sqlite3

# connect to database (this creates data.db file)
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")
