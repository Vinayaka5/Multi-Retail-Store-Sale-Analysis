import mysql.connector
from datetime import date, timedelta

# same credentials as before
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # or your user
    password="leodas",
    database="retail_dashboard"
)
cur = conn.cursor()

# get store ids
cur.execute("SELECT id, name FROM stores")
stores = cur.fetchall()

today = date.today()
days = [today - timedelta(days=2),
        today - timedelta(days=1),
        today]

sample_products = [
    ("Leather Wallet", 1500.00),
    ("Canvas Bag", 2500.00),
    ("Travel Journal", 800.00),
    ("Keychain", 300.00),
    ("Backpack", 3500.00),
]

# simple sample: for each store, each day, a few random-like rows
for store_id, store_name in stores:
    qty_base = store_id  # just to vary a bit
    for d in days:
        for i, (pname, price) in enumerate(sample_products, start=1):
            qty = qty_base + i  # 2,3,4...
            amount = qty * price
            cur.execute(
                """
                INSERT INTO sales (store_id, product_name, sale_date, quantity, amount)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (store_id, pname, d, qty, amount)
            )

conn.commit()
print("Inserted sample sales for 3 days.")
cur.close()
conn.close()
