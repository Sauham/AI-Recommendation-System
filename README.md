# 🧠 AI Recommendation System

This project is a **multi-agent AI system** designed for hyper-personalized product recommendations in an e-commerce setting. It leverages customer profiling, browsing behavior, purchase history, and product intelligence to deliver tailored recommendations using a modular, extensible agent-based framework.

---

## 🚀 Features

- 🔍 **Customer Behavior Analysis**: Understand customer interests, segment profiles.
- 🤖 **Multi-Agent Architecture**: Separate agents for customer, product, and recommendation logic.
- 📊 **Smart Recommendations**: Tailored product suggestions based on user preferences and behavior.
- 🧠 **Long-Term Memory**: SQLite used for persistent customer and product state storage.
- 💡 **Interactive Frontend**: Simple web interface to input customer IDs and view recommendations.
- 📁 **Product Detail Linking**: Click on recommended products to view detailed attributes.

---

## 🧬 Tech Stack

- **Backend**: Python, FastAPI
- **Frontend**: HTML/CSS, JavaScript (Vanilla)
- **Database**: SQLite
- **Multi-Agent System**: Custom agents with modular design
- **Others**: Pandas, JSON

---

## 📁 Project Structure

```
AI-Recommendation-System/
│
├── app/
│   ├── app.py              # FastAPI server
│   ├── customer_agent.py   # Customer logic & memory
│   ├── product_agent.py    # Product intelligence
│   ├── recommender_agent.py# Core recommendation engine
│   ├── database/           # SQLite DB files
│   └── templates/          # HTML frontend files
│
├── data/
│   ├── customers.csv       # Customer dataset
│   └── products.csv        # Product dataset
│
└── README.md               # You're here!
```

---

## 🧪 How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Sauham/AI-Recommendation-System.git
   cd AI-Recommendation-System/app
   ```

2. **Create a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server**  
   ```bash
   uvicorn app:app --reload
   ```

5. **Visit**  
   Open your browser and go to:  
   `http://127.0.0.1:8000`

---

## 📌 Example

**Input**:
```json
Customer ID: C1000
```

**Output**:
```json
[
  {
    "product_id": "P2231",
    "category": "Fitness",
    "subcategory": "Dumbbells",
    "brand": "Brand B",
    "price": 3418,
    "recommendation_score": 1
  },
  ...
]
```

Click on any product to view full details!

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

---

Made with ❤️ by [Sauham](https://github.com/Sauham)

