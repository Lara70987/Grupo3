import sqlite3

DB_NAME = "banco.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    favorite BOOLEAN DEFAULT 0
);
""")

conn.commit()
conn.close()

