import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Text corpus for chatbot knowledge base
corpus = """
Chatbots are software applications used to conduct online chat conversations.
They are often used in customer service, sales, and as virtual assistants.
Chatbots can be rule-based or use artificial intelligence.
Natural Language Processing allows the chatbot to understand and respond in human language.
"""

# Preprocessing functions
lemmatizer = nltk.stem.WordNetLemmatizer()
sent_tokens = nltk.sent_tokenize(corpus.lower())

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower()))

# Response function
def chatbot_response(user_input):
    sent_tokens.append(user_input)
    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = vectorizer.fit_transform(sent_tokens)
    
    similarity = cosine_similarity(tfidf[-1], tfidf)
    index = similarity.argsort()[0][-2]
    
    flat = similarity.flatten()
    flat.sort()
    score = flat[-2]
    
    sent_tokens.pop()
    
    if score > 0.2:
        return sent_tokens[index]
    else:
        return "I'm sorry, I don't understand that."

# Chat loop
print("Chatbot: Hello! Ask me anything about chatbots. Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot:", chatbot_response(user_input))
