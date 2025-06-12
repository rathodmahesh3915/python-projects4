import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('spam.csv', sep='\t', names=['label', 'message'])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ✅ Predict custom messages FIRST
samples = [
    "Free iPhone winner! Claim now!",
    "Let's meet for lunch tomorrow.",
    "URGENT! Your account has been suspended.",
    "Are you coming to the meeting?"
]

samples_vec = vectorizer.transform(samples)
preds = model.predict(samples_vec)

print("\nCustom Message Predictions:")
for msg, pred in zip(samples, preds):
    print(f"Message: {msg}")
    print("Prediction:", "Spam" if pred == 1 else "Ham")
    print("------")

# ✅ Plot confusion matrix LAST
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Ham (Predicted)', 'Spam (Predicted)'],
            yticklabels=['Ham (Actual)', 'Spam (Actual)'])
plt.title('Confusion Matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.show()

# ✅ Optional: Pause so terminal stays open
input("Press Enter to close...")
