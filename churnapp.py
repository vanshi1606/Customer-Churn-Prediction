import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

# LOAD MODEL
model = pickle.load(open("churn_model.pkl", "rb"))

# PAGE CONFIG

st.set_page_config(layout="wide")
st.title(" Customer Churn Prediction Dashboard")
# LAYOUT (60% - 40%)
col1, col2 = st.columns([3, 2])

with col1:

    st.markdown("### 🧾 Customer Details")

    c1, c2 = st.columns(2)

    with c1:
        tenure = st.slider("Tenure (Months)", 0, 72, 12)
        MonthlyCharges = st.slider("Monthly Charges", 0.0, 1000.0, 100.0)

    with c2:
        TotalCharges = st.slider("Total Charges", 0.0, 12000.0, 1000.0)

    st.markdown("### ⚙️ Services")

    c3, c4, c5 = st.columns(3)

    with c3:
        Contract = st.selectbox("Contract",
                                ["Month-to-Month", "One Year", "Two Year"])

    with c4:
        InternetService = st.selectbox("Internet",
                                      ["DSL", "Fiber Optic", "No Internet"])

    with c5:
        TechSupport = st.selectbox("Tech Support", ["No", "Yes"])

    # Encoding
    Contract = {"Month-to-Month": 0, "One Year": 1, "Two Year": 2}[Contract]
    InternetService = {"DSL": 0, "Fiber Optic": 1, "No Internet": 2}[InternetService]
    TechSupport = {"No": 0, "Yes": 1}[TechSupport]

    st.markdown("")

    if st.button("🔍 Predict Churn", use_container_width=True):

        data = [[0, 0, 0, 0, tenure, 1, 0, InternetService, 0, 0, 0,
                 TechSupport, 0, 0, Contract, 1, 2,
                 MonthlyCharges, TotalCharges]]

        df = pd.DataFrame(data)

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]

        st.session_state["pred"] = pred
        st.session_state["prob"] = prob

    # ---------------- RESULT ----------------
    if "prob" in st.session_state:

        prob = st.session_state["prob"]
        pred = st.session_state["pred"]

        st.markdown("---")
        st.markdown("### Prediction Summary")

        if pred == 1:
            st.error(f"⚠️ Customer will CHURN ({prob:.2f})")
        else:
            st.success(f"✅ Customer will STAY ({prob:.2f})")

        # Risk Level
        if prob > 0.7:
            st.error("🔴 High Risk")
        elif prob > 0.4:
            st.warning("🟡 Medium Risk")
        else:
            st.success("🟢 Low Risk")

        # Recommendations
        st.markdown("### 💡 Recommendations")

        if prob > 0.7:
            st.info("""
            - Offer discounts  
            - Improve service quality  
            - Immediate customer outreach  
            """)
        elif prob > 0.4:
            st.info("""
            - Provide loyalty benefits  
            - Increase engagement  
            """)
        else:
            st.info("""
            - Maintain service  
            - Upsell premium plans  
            """)

# ================= RIGHT SIDE (VISUALIZATION) =================
with col2:

    if "prob" in st.session_state:

        prob = st.session_state["prob"]

        st.markdown("### 📊 Insights")

        g1, g2 = st.columns(2)
        g3, g4 = st.columns(2)

        chart_size = (3, 2)  

        # -------- BAR --------
        with g1:
            fig, ax = plt.subplots(figsize=chart_size)
            ax.bar(["Stay", "Churn"],
                   [1 - prob, prob],
                   color=["#4CAF50", "#F44336"])
            ax.set_title("Churn vs Stay", fontsize=9)
            ax.tick_params(labelsize=8)
            st.pyplot(fig)

        # -------- GAUGE --------
        with g2:
            fig, ax = plt.subplots(figsize=chart_size)

            theta = np.linspace(0, np.pi, 100)

            ax.fill_between(np.cos(theta[:33]), 0, np.sin(theta[:33]), color="#F44336")
            ax.fill_between(np.cos(theta[33:66]), 0, np.sin(theta[33:66]), color="#FFC107")
            ax.fill_between(np.cos(theta[66:]), 0, np.sin(theta[66:]), color="#4CAF50")

            angle = np.pi * prob
            ax.plot([0, np.cos(angle)], [0, np.sin(angle)], lw=2)

            ax.text(0, -0.2, "Risk Meter", ha='center', fontsize=8)
            ax.text(0, -0.35, f"{int(prob*100)}%", ha='center', fontsize=9)

            ax.axis('off')
            st.pyplot(fig)

        # -------- PROFILE --------
        with g3:
            fig2, ax2 = plt.subplots(figsize=chart_size)
            ax2.bar(["Tenure", "Monthly", "Total"],
                    [tenure, MonthlyCharges, TotalCharges],
                    color="#2196F3")
            ax2.set_title("Customer Profile", fontsize=9)
            ax2.tick_params(labelsize=8)
            st.pyplot(fig2)

        # -------- PIE --------
        with g4:
            fig3, ax3 = plt.subplots(figsize=chart_size)
            ax3.pie([1 - prob, prob],
                    labels=["Stay", "Churn"],
                    colors=["#4CAF50", "#F44336"],
                    autopct="%1.1f%%",
                    textprops={'fontsize': 8})
            ax3.set_title("Distribution", fontsize=9)
            st.pyplot(fig3)