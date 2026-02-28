def calculate_financials(income, expenses, debt):

    savings = income - expenses
    savings_ratio = (savings / income) * 100 if income > 0 else 0
    debt_ratio = (debt / income) * 100 if income > 0 else 0

    return savings, savings_ratio, debt_ratio