import pandas as pd
import sqlite3

# Load CSVs
customer_df = pd.read_csv("data/customer_data_collection.csv")
product_df = pd.read_csv("data/product_recommendation_data.csv")

# Connect to DB
conn = sqlite3.connect("db/ecommerce.db")

# Write to tables
customer_df.to_sql("customers", conn, if_exists="replace", index=False)
product_df.to_sql("products", conn, if_exists="replace", index=False)

conn.close()
print("Database setup complete.")
