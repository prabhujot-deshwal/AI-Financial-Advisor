from config import client

def get_ai_advice(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"


# ---- TEST BLOCK ----
if __name__ == "__main__":
    print("Testing Gemini API...")
    result = get_ai_advice("Give 3 tips to save money.")
    print(result)