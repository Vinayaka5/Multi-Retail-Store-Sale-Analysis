from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# use same credentials that worked in test_mysql_connection.py
db = mysql.connector.connect(
    host="localhost",
    user="root",              # or your user
    password="leodas",
    database="retail_dashboard"
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def dashboard():
    # total sales by store
    cursor.execute("""
        SELECT s.name AS store_name,
               SUM(sa.amount) AS total_amount
        FROM sales sa
        JOIN stores s ON sa.store_id = s.id
        GROUP BY s.id, s.name
        ORDER BY total_amount DESC
    """)
    sales_by_store = cursor.fetchall()

    # top products overall
    cursor.execute("""
        SELECT product_name,
               SUM(quantity) AS total_qty,
               SUM(amount) AS total_amount
        FROM sales
        GROUP BY product_name
        ORDER BY total_qty DESC
        LIMIT 10
    """)
    top_products = cursor.fetchall()

    return render_template(
        "dashboard.html",
        sales_by_store=sales_by_store,
        top_products=top_products
    )

if __name__ == "__main__":
    app.run(debug=True)
