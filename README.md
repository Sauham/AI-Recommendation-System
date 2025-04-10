# 🛍️ Multi-Agent AI Recommendation System for E-Commerce

## 🧠 Challenge Overview

In the competitive world of e-commerce, providing personalized and relevant product recommendations is key to improving customer experience, increasing conversion rates, and boosting sales.

This project addresses that challenge by building a **multi-agentic AI system** that delivers **hyper-personalized product recommendations** for an e-commerce platform. The system utilizes autonomous agents representing customers, products, and recommendation engines, which collaborate to:

- Analyze browsing behavior  
- Predict user preferences  
- Optimize the overall shopping experience  

By doing so, the system helps the e-commerce platform:

- ✅ Deliver tailored recommendations based on individual behavior and interests  
- ✅ Improve engagement  
- ✅ Increase average order value  
- ✅ Enhance customer retention  
- ✅ Drive higher conversion rates  

---

## 🧾 Current Industry Process

### 1. Customer Data Collection and Segmentation

- E-commerce teams manually collect and store customer browsing behavior, purchase history, and demographic data in databases or spreadsheets.
- Customer profiles are created based on specific attributes like age, gender, location, and purchase history.
- Customers are manually segmented into categories (e.g., frequent buyers, new visitors).

### 2. Product Recommendations

- Marketing teams manually analyze data to identify patterns and trends.
- Based on customer segmentation, they select a set of products to recommend.
- For example:
  - Frequent buyers → Related products  
  - New visitors → Popular or discounted products  

This process is time-consuming, lacks real-time personalization, and limits scalability.

---

## 🚀 Solution: Multi-Agent System

This project introduces a **multi-agent framework** where different agents communicate and collaborate to deliver personalized recommendations:

- 🤖 **CustomerAgent**: Maintains customer data and simulates user preferences.
- 📦 **ProductAgent**: Manages product information (category, price, brand, etc.).
- 🧠 **RecommendationAgent**: Uses customer and product data to compute recommendations based on collaborative and content-based filtering.
- 💾 **SQLite Database**: Acts as persistent long-term memory for all agents.

Agents interact autonomously to simulate a real-world e-commerce recommendation engine.

---

## 🛠️ Tech Stack

| Component         | Technology / Tool             |
|------------------|-------------------------------|
| Backend           | Python, Flask                 |
| Frontend          | Streamlit                     |
| Database          | SQLite                        |
| Data Processing   | Pandas, NumPy                 |
| Machine Learning  | Scikit-learn                  |
| Visualization     | Plotly, Matplotlib            |
| Architecture      | Multi-agent Python classes    |

---

## 💡 Key Features

- 🔍 Personalized product recommendations per user
- 📊 Visual insights (brand distribution, pricing trends)
- 🗂️ Real-time product filtering and interaction
- 🧠 Autonomous agent communication
- 💾 Persistent memory using SQLite
- 🎯 Streamlined UI with Streamlit

---

## 📸 Screenshots

<p align="center">
  <img src="https://user-images.githubusercontent.com/your-screenshot-link" alt="App Screenshot" width="800"/>
</p>

---

## 🧪 How It Works

1. Enter a **Customer ID** (e.g., `C1000`) on the UI.
2. System queries the database and loads customer details.
3. CustomerAgent passes info to RecommendationAgent.
4. RecommendationAgent fetches relevant products from ProductAgent.
5. Recommended products are displayed in UI with insights.

---

## ⚙️ Installation & Setup

### 🔄 Clone the Repository

```bash
git clone https://github.com/yourusername/multi-agent-recommendation-system.git
cd multi-agent-recommendation-system
```

### 📦 Install Dependencies

Make sure you have Python ≥ 3.8 and run:
```bash
pip install -r requirements.txt
```

### 🚀 Start the Application

1. Run Flask backend
From the app/ directory or root:
```bash
cd app
python app.py
```

2. Run Streamlit frontend
From your root project directory:
```bash
cd streamlit_app
streamlit run streamlit_app.py
```

---

## 📚 Project Structure
```
AI-Recommendation-System/
│   ├── __init__.py              
│   ├── customer_agent.py   
│   ├── interaction_agent.py   
│   ├── product_agent.py
│   └──recommendation_agent.py           
├── app/
│   ├── app.py   
├── data/
│   ├── customers.csv       # Customer dataset
│   └── products.csv        # Product dataset
├── db/
│    └──ecommerce.db
├── streamlit_app/
│   └── streamlit_app.py   # Streamlit frontend
├── venv/
├── check_customer.py
├── main.py
├── requirements.txt
├── setup_db.py
└── README.md               # You're here!
```

---

## 📚 License

MIT License. Feel free to fork, contribute, and adapt this project to your use case.

---

## 🙌 Contributing

Pull requests are welcome! If you find a bug or have a feature idea, open an issue or PR.

---

## ✨ Future Improvements

- Integrate with real-time user tracking
- Add collaborative filtering-based recommendations
- Support user login and personalized dashboards



