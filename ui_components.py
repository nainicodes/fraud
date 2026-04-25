import streamlit as st
import pandas as pd
import random

def render_sidebar():
    st.sidebar.title("🛡️ FraudGuard AI")
    st.sidebar.markdown("---")
    choice = st.sidebar.radio("Navigation", ["Home", "How it Works", "Live Predictor", "Quiz & Trivia"])
    return choice

def render_home():
    st.title("Financial Fraud Detection System")
    st.markdown("""
    Welcome to **FraudGuard AI**. This platform demonstrates how modern machine learning 
    identifies suspicious patterns in financial transactions.
    
    ### Why Fraud Detection Matters?
    * **$42 Billion:** Total fraud losses reported by companies globally in 2023.
    * **Real-time processing:** Systems must decide in milliseconds.
    * **Data Imbalance:** Fraudulent cases usually make up <1% of total data.
    """)
    st.image("https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=800", caption="Securing Digital Transactions")

def render_education():
    st.header("The Machine Learning Pipeline")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("1. Data Ingestion")
        st.write("Collecting transaction amounts, timestamps, and merchant IDs.")
    with col2:
        st.subheader("2. Feature Engineering")
        st.write("Calculating 'velocity' (how many swipes in 1 hour) and location consistency.")
    with col3:
        st.subheader("3. Anomaly Detection")
        st.write("Using algorithms like Random Forest or XGBoost to find outliers.")

def render_playground():
    st.header("Interactive Transaction Predictor")
    st.info("Adjust the sliders to simulate a transaction and see the AI's risk assessment.")

    col1, col2 = st.columns(2)
    with col1:
        amount = st.slider("Transaction Amount ($)", 0, 10000, 50)
        distance = st.slider("Distance from Home (miles)", 0, 5000, 5)
        is_international = st.checkbox("International Transaction?")
    
    # Simple Heuristic Logic for Demonstration
    risk_score = 0
    if amount > 5000: risk_score += 40
    if distance > 1000: risk_score += 30
    if is_international: risk_score += 20

    with col2:
        st.metric("Risk Score", f"{risk_score}%")
        if risk_score > 60:
            st.error("🚨 High Risk: Transaction Blocked")
        elif risk_score > 30:
            st.warning("⚠️ Medium Risk: Verification Required")
        else:
            st.success("✅ Low Risk: Transaction Approved")

def render_quiz():
    st.header("🧠 Trivia & Quiz")
    
    # Trivia Section
    with st.expander("💡 Did you know? (Click to expand)"):
        trivias = [
            "The first credit card fraud occurred almost as soon as the first card was issued in 1950.",
            "Synthetic Identity Fraud is the fastest-growing type of financial crime.",
            "AI can analyze over 10,000 data points per transaction in less than 300ms."
        ]
        st.write(random.choice(trivias))

    st.markdown("---")
    
    # Quiz Section
    st.subheader("Test Your Knowledge")
    q1 = st.radio("What is 'False Positive' in fraud detection?", 
                  ["A fraudulent transaction caught", "A legitimate transaction flagged as fraud", "A fraudster escaping"])
    
    if st.button("Submit Answer"):
        if q1 == "A legitimate transaction flagged as fraud":
            st.success("Correct! False positives cause 'customer friction'.")
        else:
            st.error("Try again! Think about a 'False' alarm.")
            