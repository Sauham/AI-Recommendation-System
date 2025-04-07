from flask import Flask, request, jsonify, render_template
import os
import sys
import sqlite3
# Set absolute paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
AGENTS_DIR = os.path.join(BASE_DIR, 'agents')
DB_PATH = os.path.join(BASE_DIR, 'db', 'ecommerce.db')
CUSTOMER_CSV = os.path.join(BASE_DIR, 'data', 'customer_data_collection.csv')
PRODUCT_CSV = os.path.join(BASE_DIR, 'data', 'product_recommendation_data.csv')

# Add agents to sys.path
sys.path.append(AGENTS_DIR)

from customer_agent import CustomerAgent
from product_agent import ProductAgent
from recommendation_agent import RecommendationAgent

# Initialize Flask app
app = Flask(__name__)
# Initialize agents
customer_agent = CustomerAgent(DB_PATH)
product_agent = ProductAgent(DB_PATH)
recommendation_agent = RecommendationAgent(DB_PATH)

# # Initialize agents
# customer_agent = CustomerAgent(CUSTOMER_CSV, DB_PATH)
# product_agent = ProductAgent(PRODUCT_CSV, DB_PATH)
# recommendation_agent = RecommendationAgent(DB_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    customer_id = data.get("customer_id")

    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    try:
        profile = customer_agent.get_customer_profile(customer_id)
        recommendations = recommendation_agent.recommend(profile)
        return jsonify({"customer_id": customer_id, "recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/product/<product_id>', methods=['GET'])
def get_product_details(product_id):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE Product_ID = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            columns = [description[0] for description in cursor.description]
            return jsonify(dict(zip(columns, row)))
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
