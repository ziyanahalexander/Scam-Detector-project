import streamlit as st
import joblib
import requests
import pytesseract
from PIL import Image
API_KEY = st.secrets["API_KEY"]

# Load the trained model and vectorizer once when the app starts
model = joblib.load("scam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def get_explanation(message):
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
    return response.json()["choices"][0]["message"]["content"]


# --- The actual webpage layout starts here ---

st.title("Scam Message Detector")
st.write("Paste a suspicious message, or upload a screenshot of one, to check if it looks like a scam.")

input_method = st.radio("How would you like to check a message?", ["Paste text", "Upload a screenshot"])

message = ""

if input_method == "Paste text":
    message = st.text_area("Message to check:", height=150)
else:
    uploaded_image = st.file_uploader("Upload a screenshot", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded screenshot", width=400)
        with st.spinner("Reading text from image..."):
            message = pytesseract.image_to_string(image)
        st.write("**Text found in image:**")
        st.write(message)

if st.button("Check this message"):
    if message.strip() == "":
        st.warning("Please paste a message or upload a screenshot first.")
    else:
        message_vec = vectorizer.transform([message])
        prediction = model.predict(message_vec)[0]

        if prediction == 1:
            st.error("⚠️ This looks like a SCAM")
            with st.spinner("Getting an explanation..."):
                explanation = get_explanation(message)
            st.write("**Why it's suspicious:**")
            st.write(explanation)
        else:
            st.success("✅ This does not look like a scam")       
