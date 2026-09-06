# Scam Message Detector

A machine-learning and AI-powered tool that helps users identify potentially fraudulent messages and understand why they may be suspicious.

## About the Project

Scam Message Detector is a tool designed to help people identify potentially fraudulent or suspicious messages. While it can be used by anyone, I built the project with older adults and people who may be less familiar with navigating the internet in mind.

Users can paste the text of a suspicious message or upload a screenshot for analysis. Rather than only providing a scam or non-scam classification, the tool provides a short, plain-language explanation when a message is flagged, helping users understand the warning signs themselves.

## Features

- Paste suspicious messages directly into the app
- Upload screenshots of messages for analysis
- Extract text from screenshots using OCR
- Classify messages as likely scam or not scam
- Generate plain-language explanations for messages identified as suspicious
- Simple interface designed with accessibility and ease of use in mind

## How It Works

The application uses a machine-learning model to classify messages as scam or non-scam.

Message text is converted into numerical features using TF-IDF and analyzed by a Logistic Regression classifier. If a screenshot is uploaded, Tesseract OCR first extracts the text from the image.

When a message is classified as a likely scam, Llama 3.1 is used through the Hugging Face API to generate a short, plain-language explanation of what makes the message suspicious.

## Tech Stack

- Python
- Streamlit
- scikit-learn
- Pandas
- TF-IDF Vectorization
- Logistic Regression
- Tesseract OCR
- Pillow
- Hugging Face API
- Meta Llama 3.1

## Machine Learning Model

The scam detection model was built using a labeled dataset of phishing and non-phishing messages. The data is divided into training and testing sets, and message text is transformed using TF-IDF vectorization.

A Logistic Regression classifier is then trained on the transformed text and evaluated using held-out test data. The trained model and vectorizer are saved and loaded by the Streamlit application to classify new messages.

## Running the Project

Install the required Python dependencies:

    pip install -r requirements.txt

Then start the Streamlit application:

    streamlit run app.py

## Future Improvements

- Add confidence scores to scam predictions
- Expand the model's ability to recognize more subtle scam techniques
- Improve screenshot and image processing
- Continue improving accessibility for users with less experience navigating the internet
- Evaluate the model using additional metrics such as precision, recall, and F1 score
