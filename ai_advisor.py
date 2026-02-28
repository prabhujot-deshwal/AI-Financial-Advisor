from config import client

def get_ai_advice(prompt):

    if client:
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            return response.text
        except:
            pass

    # Demo fallback response
    return """
    📊 Budget Advice:
    - Maintain at least 20% savings rate.
    - Reduce unnecessary expenses.
    
    💰 Investment Advice:
    - Invest in SIPs with moderate risk.
    - Diversify across equity and debt.
    
    🛡️ Debt Strategy:
    - Pay high-interest loans first.
    """