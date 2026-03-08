def get_ai_advice(question):

    question = question.lower()

    if "investment" in question:
        return """
📈 Investment Advice:
• Start SIP in mutual funds.
• Diversify your portfolio.
• Invest for the long term.
• Avoid emotional investing.
"""

    elif "save money" in question or "saving" in question:
        return """
💰 Saving Tips:
• Follow the 50/30/20 rule.
• Track your monthly expenses.
• Avoid unnecessary spending.
• Build an emergency fund.
"""

    elif "debt" in question:
        return """
💳 Debt Advice:
• Pay high-interest debt first.
• Avoid unnecessary loans.
• Use credit cards responsibly.
"""

    elif "budget" in question:
        return """
📊 Budgeting Advice:
• Track income and expenses.
• Set monthly financial goals.
• Limit impulse purchases.
"""

    else:
        return """
🤖 General Financial Advice:

• Save at least 20% of your income.
• Invest consistently.
• Diversify your investments.
• Keep an emergency fund.
"""