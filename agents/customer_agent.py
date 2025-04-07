import sqlite3

class CustomerAgent:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_customer_profile(self, customer_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE Customer_ID=?", (customer_id,))
        row = cursor.fetchone()
        conn.close()

        if row is None:
            raise ValueError("Customer not found")

        columns = [desc[0] for desc in cursor.description]
        profile = dict(zip(columns, row))
        return profile
