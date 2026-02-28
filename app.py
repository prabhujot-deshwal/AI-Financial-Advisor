import streamlit as st
import matplotlib.pyplot as plt
from finance_analysis import calculate_financials
from ai_advisor import get_ai_advice

st.set_page_config(page_title="AI Financial Advisor", layout="wide")

# ---- Load CSS ----
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💰 AI Financial Advisor Dashboard")

st.sidebar.header("📥 Enter Financial Details")

income = st.sidebar.number_input("Monthly Income (₹)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0)
debt = st.sidebar.number_input("Total Debt (₹)", min_value=0)

goal_amount = st.sidebar.number_input("🎯 Financial Goal (₹)", min_value=0)
goal_years = st.sidebar.number_input("Goal Duration (Years)", min_value=1)

if st.sidebar.button("Analyze Financial Health"):

    savings, savings_ratio, debt_ratio = calculate_financials(income, expenses, debt)

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Savings (₹)", savings)
    col2.metric("📊 Savings Ratio (%)", round(savings_ratio, 2))
    col3.metric("⚠️ Debt Ratio (%)", round(debt_ratio, 2))

    st.subheader("📈 Income vs Expenses")

    fig, ax = plt.subplots()
    ax.bar(["Income", "Expenses", "Savings"], [income, expenses, savings])
    st.pyplot(fig)

    if goal_amount > 0:
        monthly_needed = goal_amount / (goal_years * 12)

        st.subheader("🎯 Goal Planning")
        st.write(
            f"You need to invest approximately ₹{round(monthly_needed,2)} per month to reach your goal."
        )

    prompt = f"""
    Income: {income}
    Expenses: {expenses}
    Debt: {debt}
    Savings Ratio: {savings_ratio}
    """

    advice = get_ai_advice(prompt)

    # --- AI Advice Section ---
    st.subheader("🤖 AI Financial Advice")
    st.write(advice)

    # --- AI Chat Section ---
    st.subheader("💬 Ask AI Financial Question")

    user_question = st.text_input("Enter your financial question:")

    if user_question:
        chat_response = get_ai_advice(user_question)
        st.write(chat_response)