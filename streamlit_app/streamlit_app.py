import streamlit as st
import requests

FLASK_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="E-commerce Recommender", layout="wide")
st.title("🛍️ Multi-Agent E-commerce Recommender")

st.markdown("### 🔎 Enter a Customer ID to Get Personalized Recommendations")

customer_id = st.text_input("Customer ID", placeholder="e.g. C1000")

if st.button("🎯 Get Recommendations"):
    if not customer_id.strip():
        st.warning("⚠️ Please enter a valid Customer ID.")
    else:
        with st.spinner("🔄 Fetching recommendations from backend..."):
            try:
                res = requests.post(f"{FLASK_URL}/recommend", json={"customer_id": customer_id})
                if res.status_code == 200:
                    data = res.json()
                    recommendations = data.get("recommendations", [])

                    if recommendations:
                        st.success(f"✅ {len(recommendations)} recommendations received for Customer ID: `{customer_id}`")
                        st.markdown("## 🎁 Recommended Products")

                        st.markdown("""
                            <style>
                            .card {
                                background: rgba(255, 255, 255, 0.05);
                                border-radius: 12px;
                                padding: 20px;
                                margin-bottom: 20px;
                                margin-right: 10px;
                                margin-left: 10px;
                                color: white;
                                border: 1px solid rgba(255, 255, 255, 0.1);
                                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
                                height: 220px;
                            }
                            .card-title {
                                font-weight: 700;
                                font-size: 18px;
                                margin-bottom: 10px;
                                color: #FBBF24;
                            }
                            .card-sub {
                                font-size: 14px;
                                margin-bottom: 6px;
                                opacity: 0.85;
                            }
                            </style>
                        """, unsafe_allow_html=True)

                        
                        num_cols = 3
                        rows = [recommendations[i:i+num_cols] for i in range(0, len(recommendations), num_cols)]

                        for row in rows:
                            cols = st.columns(num_cols)
                            for idx, rec in enumerate(row):
                                with cols[idx]:
                                    st.markdown(
                                        f"""
                                        <div class="card">
                                            <div class="card-title">🆔 {rec.get("product_id")}</div>
                                            <div class="card-sub">🏷️ Brand: <strong>{rec.get("brand")}</strong></div>
                                            <div class="card-sub">📚 Category: {rec.get("category")} > {rec.get("subcategory")}</div>
                                            <div class="card-sub">💰 Price: ₹{rec.get("price")}</div>
                                            <div class="card-sub">📊 Score: {rec.get("recommendation_score")}</div>
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                    else:
                        st.info(f"No recommendations found for Customer ID `{customer_id}`.")
                else:
                    st.error(f"❌ Backend error: {res.json().get('error', 'Unknown error')}")
            except Exception as e:
                st.error(f"🚨 Failed to fetch recommendations: {str(e)}")
