import joblib
import requests

from api_key import API_KEY

# 1. Load your already-trained model and vectorizer
model = joblib.load("scam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def check_message(message):
    # 2. Run the model's prediction
    message_vec = vectorizer.transform([message])
    prediction = model.predict(message_vec)[0]
    verdict = "SCAM" if prediction == 1 else "NOT SCAM"

    print(f"Message: {message}")
    print(f"Verdict: {verdict}")

    # 3. Only ask the AI to explain if it's flagged as a scam
    if prediction == 1:
        prompt = f"""A machine learning model flagged this message as a likely scam:

"{message}"

In 2-3 short, plain-language sentences suitable for an older adult with limited tech experience, explain what specifically makes this message suspicious. Avoid technical jargon. Be direct and reassuring, not alarming."""

        response = requests.post(
            "https://router.huggingface.co/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        explanation = response.json()["choices"][0]["message"]["content"]
        print(f"Why it's suspicious: {explanation}")

    print()


# 4. Try it on a few examples
check_message("URGENT: Your bank account has been suspended, click here to verify")
check_message("Can you send me the notes from today's meeting?")
