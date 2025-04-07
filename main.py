import os
import pandas as pd
import sqlite3

def create_database(db_path='db/ecommerce.db'):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create Customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            browsing_history TEXT,
            purchase_history TEXT
        )
    ''')
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            description TEXT,
            price REAL,
            rating REAL
        )
    ''')
    conn.commit()
    conn.close()

def load_data_into_db(db_path='db/ecommerce.db'):
    conn = sqlite3.connect(db_path)
    
    # Load CSVs
    customer_df = pd.read_csv('data/customer_data_collection.csv')
    product_df = pd.read_csv('data/product_recommendation_data.csv')
    
    # Basic cleaning (e.g., drop missing values)
    customer_df.dropna(inplace=True)
    product_df.dropna(inplace=True)
    
    # Write data to the database
    customer_df.to_sql('Customers', conn, if_exists='replace', index=False)
    product_df.to_sql('Products', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    print("Creating database...")
    create_database()
    print("Loading data into database...")
    load_data_into_db()
    print("Database setup complete.")
