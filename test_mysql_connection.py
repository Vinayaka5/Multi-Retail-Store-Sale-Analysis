import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",              # change if your MySQL user is different
    password="leodas"
)

print("Connected to MySQL!")
conn.close()
