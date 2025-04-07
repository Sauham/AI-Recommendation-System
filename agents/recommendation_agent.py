import sqlite3

class RecommendationAgent:
    def __init__(self, db_path):
        self.db_path = db_path

    def recommend(self, customer_profile, limit=5):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT Product_ID, Category, Subcategory, Price, Brand, 
                   Probability_of_Recommendation
            FROM products
            ORDER BY Probability_of_Recommendation DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "product_id": row[0],
                "category": row[1],
                "subcategory": row[2],
                "price": row[3],
                "brand": row[4],
                "recommendation_score": row[5]
            }
            for row in rows
        ]
