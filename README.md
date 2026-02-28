# AI Financial Advisor

## Overview

AI Financial Advisor is a smart financial planning application that helps users analyze their financial health and receive personalized financial advice. The system uses **Google Gemini AI** to generate intelligent insights based on user inputs such as income, expenses, savings, and financial goals.

The goal of this project is to simplify financial planning and help users make better financial decisions through AI-driven recommendations.

---

## Features

* Personalized financial advice using AI
* Monthly income and expense analysis
* Budget planning assistance
* Savings and investment suggestions
* Real-time financial insights
* Interactive and user-friendly interface

---

## Tech Stack

* **Frontend / UI:** Streamlit
* **Backend:** Python
* **AI Model:** Google Gemini API
* **Data Handling:** Pandas
* **Visualization:** Matplotlib / Streamlit Charts

---

## Project Structure

```
AI-Financial-Advisor
│
├── app.py                # Main Streamlit application
├── financial_logic.py    # Financial calculations
├── gemini_integration.py # Gemini AI API integration
├── requirements.txt      # Required Python packages
└── README.md             # Project documentation
```

---

## How It Works

1. User enters financial details such as:

   * Monthly income
   * Expenses
   * Savings
   * Financial goals

2. The system analyzes the financial data.

3. Google Gemini AI generates personalized financial recommendations.

4. The application displays:

   * Budget suggestions
   * Savings insights
   * Investment advice

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/AI-Financial-Advisor.git
```

### 2. Navigate to the Project Folder

```
cd AI-Financial-Advisor
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add Gemini API Key

Create an environment variable or add your API key inside the code.

Get your API key from:
https://makersuite.google.com/app/apikey

---

## Running the Application

Run the Streamlit app:

```
streamlit run app.py
```

The application will start on:

```
http://localhost:8501
```

---

## Future Enhancements

* Expense tracking dashboard
* Investment portfolio recommendations
* Financial risk analysis
* Multi-user financial profiles
* Predictive financial analytics

---

## Use Cases

* Students planning monthly budgets
* Professionals managing savings and investments
* Individuals looking for AI-driven financial advice

---

## License

This project is created for educational purposes as part of the **SkillWallet Generative AI Program**.

---
