import streamlit as st
import matplotlib.pyplot as plt
from finance_analysis import calculate_financials
from ai_advisor import get_ai_advice

st.set_page_config(page_title="AI Financial Advisor", layout="wide")

# ---- Load CSS ----
try:
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

st.title("💰 AI Financial Advisor Dashboard")

# ---- Sidebar Inputs ----
st.sidebar.header("📥 Enter Financial Details")

income = st.sidebar.number_input("Monthly Income (₹)", min_value=0, value=0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0, value=0)
debt = st.sidebar.number_input("Total Debt (₹)", min_value=0, value=0)

goal_amount = st.sidebar.number_input("🎯 Financial Goal (₹)", min_value=0, value=0)
goal_years = st.sidebar.number_input("Goal Duration (Years)", min_value=1, value=1)

analyze_button = st.sidebar.button("Analyze Financial Health")

# ---- Financial Analysis ----
if analyze_button:

    savings, savings_ratio, debt_ratio = calculate_financials(income, expenses, debt)

    st.subheader("📊 Financial Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Savings (₹)", savings)
    col2.metric("📈 Savings Ratio (%)", round(savings_ratio, 2))
    col3.metric("⚠️ Debt Ratio (%)", round(debt_ratio, 2))

    # ---- Chart ----
    st.subheader("📊 Income vs Expenses")

    fig, ax = plt.subplots()
    ax.bar(["Income", "Expenses", "Savings"], [income, expenses, savings])
    ax.set_ylabel("Amount (₹)")
    st.pyplot(fig)

    # ---- Goal Planning ----
    if goal_amount > 0:
        monthly_needed = goal_amount / (goal_years * 12)

        st.subheader("🎯 Goal Planning")
        st.info(
            f"You need to invest approximately ₹{round(monthly_needed,2)} per month to reach your goal."
        )

    # ---- AI Advice Section ----
    prompt = f"""
    Income: {income}
    Expenses: {expenses}
    Debt: {debt}
    Savings Ratio: {savings_ratio}
    """

    advice = get_ai_advice(prompt)

    st.subheader("🤖 AI Financial Advice")
    st.success(advice)

# ---- Ask AI Question Section ----
st.subheader("💬 Ask AI Financial Question")

question_options = [
    "How to start investing?",
    "How to save more money?",
    "How to manage debt?",
    "How to create a monthly budget?",
    "General financial advice"
]

selected_question = st.selectbox("Choose a question", question_options)

if st.button("Get AI Advice"):
    response = get_ai_advice(selected_question)
    st.success(response)