import sqlite3
import pandas as pd
import os
class ProductAgent:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_all_products(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql("SELECT * FROM products", conn)
        conn.close()
        return df
