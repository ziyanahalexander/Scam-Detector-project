import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load the data
df = pd.read_csv("phishing_email.csv")

# 2. Drop rows with missing message text, just in case
df = df.dropna(subset=["text_combined"])

# 3. Split into inputs (X) and answers (y)
X = df["text_combined"]
y = df["label"]

# 4. Split into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Turn the text into numbers the model can understand
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 6. Train the model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# 7. Test how well it did
predictions = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy * 100:.2f}%")

# 8. Try it on your own example messages
test_messages = [
    "URGENT: Your bank account has been suspended, click here to verify",
    "Apply in one minute, work from home and earn 500,000",
    "Congratulations! You've won a free iPhone, claim your prize now",
    "Can you send me the notes from today's meeting?"
]

test_vec = vectorizer.transform(test_messages)
test_predictions = model.predict(test_vec)

print("\n--- Testing custom messages ---")
for message, prediction in zip(test_messages, test_predictions):
    result = "SCAM" if prediction == 1 else "NOT SCAM"
    print(f"Message: {message}\nPrediction: {result}\n")
