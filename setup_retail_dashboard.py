import mysql.connector

# use the SAME user/password that worked earlier
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # or your user
    password="leodas"
)
cur = conn.cursor()

# 1) Create database
cur.execute("CREATE DATABASE IF NOT EXISTS retail_dashboard")

# 2) Use that database
cur.execute("USE retail_dashboard")

# 3) Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS stores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    sale_date DATE NOT NULL,
    quantity INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(id)
)
""")

# 4) Insert 5 stores if empty
cur.execute("SELECT COUNT(*) FROM stores")
(count_stores,) = cur.fetchone()

if count_stores == 0:
    cur.executemany(
        "INSERT INTO stores (name) VALUES (%s)",
        [
            ("Nappa Dori MG Road",),
            ("Nappa Dori Indiranagar",),
            ("Nappa Dori Koramangala",),
            ("Nappa Dori Mall 1",),
            ("Nappa Dori Mall 2",),
        ]
    )
    conn.commit()

print("Database + tables + stores ready.")
cur.close()
conn.close()
