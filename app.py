import streamlit as st
from finance_analysis import calculate_financials
from ai_advisor import get_ai_advice

st.set_page_config(page_title="AI Financial Advisor", layout="wide")

st.title("💰 AI Financial Advisor")

st.sidebar.header("Enter Financial Details")

income = st.sidebar.number_input("Monthly Income (₹)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0)
debt = st.sidebar.number_input("Total Debt (₹)", min_value=0)

if st.sidebar.button("Analyze"):

    savings, savings_ratio, debt_ratio = calculate_financials(income, expenses, debt)

    st.subheader("📊 Financial Overview")
    st.metric("Savings (₹)", savings)
    st.metric("Savings Ratio (%)", round(savings_ratio, 2))
    st.metric("Debt Ratio (%)", round(debt_ratio, 2))

    prompt = f"""
    User Income: {income}
    Expenses: {expenses}
    Debt: {debt}
    Savings Ratio: {savings_ratio}
    """

    advice = get_ai_advice(prompt)

    st.subheader("🤖 AI Financial Advice")
    st.write(advice)