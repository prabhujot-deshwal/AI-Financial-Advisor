def get_ai_advice(prompt):
    prompt = prompt.lower()

    if "save" in prompt:
        return """
💰 Tips to Save Money:
1. Follow the 50/30/20 rule (needs, wants, savings).
2. Track your monthly expenses.
3. Avoid unnecessary subscriptions.
4. Build an emergency fund.
"""

    elif "invest" in prompt:
        return """
📈 Investment Advice:
1. Start SIP in mutual funds.
2. Diversify your portfolio.
3. Invest for long term (5–10 years).
4. Avoid emotional investing.
"""

    elif "debt" in prompt:
        return """
💳 Debt Management Tips:
1. Pay high-interest debt first.
2. Avoid unnecessary loans.
3. Use credit cards responsibly.
"""

    else:
        return """
🤖 AI Financial Advisor

General Financial Tips:
• Save at least 20% of your income.
• Invest consistently.
• Diversify investments.
• Keep an emergency fund.
"""