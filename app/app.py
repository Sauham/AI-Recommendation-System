import os, sys
from flask import Flask, request, jsonify, render_template
import sqlite3

# Setup base paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
AGENTS_DIR = os.path.join(PARENT_DIR, "agents")
DB_PATH = os.path.join(PARENT_DIR, "db", "ecommerce.db")

sys.path.append(AGENTS_DIR)

from customer_agent import CustomerAgent
from product_agent import ProductAgent
from recommendation_agent import RecommendationAgent

app = Flask(__name__)

# Initialize agents
customer_agent = CustomerAgent(DB_PATH)
product_agent = ProductAgent(DB_PATH)
recommendation_agent = RecommendationAgent(DB_PATH)

@app.route("/")
def index():
    return "Flask API is running."

@app.route("/recommend", methods=["POST"])
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

@app.route("/product/<product_id>", methods=["GET"])
def get_product_details(product_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE Product_ID = ?", (product_id,))
        row = cursor.fetchone()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        if row:
            return jsonify(dict(zip(columns, row)))
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
