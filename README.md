This project is a small multi‑store retail sales analytics dashboard that I built using Python (Flask), MySQL, and HTML/CSS to understand which store is performing best and which 
products are moving fastest over a short time period. It is designed for an owner of a brand like Nappa Dori who wants a simple internal tool to compare daily sales across multiple 
outlets without using complex BI tools or spreadsheets.

The backend is implemented with Flask, which exposes a basic route (/) that connects to a MySQL database, runs aggregation queries, and renders the results into an HTML template. 
I created a separate setup script in Python to programmatically create the retail_dashboard database, define stores and sales tables, and insert initial store records, 
so the environment can be recreated quickly on any local machine without manually clicking in database tools.

For data modeling, I designed a simple schema with a stores table (store id, store name) and a sales table (store id, product name, sale date, quantity, amount), 
linked via a foreign key. Using SQL concepts like JOIN, GROUP BY, and SUM, the application calculates total revenue per store and also aggregates product‑level performance, 
which mirrors common retail KPI dashboard patterns used in real businesses for decision‑making.

The frontend uses a lightweight HTML/CSS dashboard layout rendered through Flask’s Jinja2 templating system, presenting two main tables: “Sales by Store” and “Top Products”. 
This structure makes it easy to visually compare which store generates the highest sales and which products have the highest quantity and revenue over the sample three‑day period, 
while still being simple enough for a beginner‑level full‑stack project.

Additional Python scripts insert a few days of sample sales data for five stores, allowing the dashboard to show realistic numbers immediately after setup. 
Through this project I practiced end‑to‑end skills: connecting Python to MySQL, handling credentials and connection errors, designing a small relational schema, writing aggregation queries, 
building a Flask route, and integrating backend data into an HTML template to create a functional internal analytics tool.
