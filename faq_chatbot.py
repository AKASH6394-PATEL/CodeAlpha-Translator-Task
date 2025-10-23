import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --- 1. अपना Q&A डेटा यहाँ डालें ---
# आप इस लिस्ट को अपने टॉपिक के हिसाब से बदल सकते हैं
faqs = {
    "What is Flutter?": "Flutter is a UI toolkit developed by Google for building natively compiled applications for mobile, web, and desktop from a single codebase.",
    "What is a Widget in Flutter?": "In Flutter, almost everything is a widget. Widgets are the basic building blocks of a user interface. Examples include Text, Row, Column, Container, etc.",
    "What programming language does Flutter use?": "Flutter uses the Dart programming language.",
    "Is Flutter free?": "Yes, Flutter is a free and open-source project.",
    "How does Hot Reload work?": "Hot Reload allows you to quickly see the changes you make to your code reflected in the app without restarting the entire application, speeding up development.",
    "What is State Management?": "State management refers to how you manage the data (state) that your application uses and displays. Flutter offers various approaches like Provider, Riverpod, BLoC, etc." # नया Q&A
}

# सवालों की लिस्ट अलग निकाल लें
questions = list(faqs.keys())

# --- 2. टेक्स्ट को वेक्टर में बदलें (TF-IDF) ---
vectorizer = TfidfVectorizer().fit(questions)
question_vectors = vectorizer.transform(questions)

# --- 3. सबसे मिलता-जुलता सवाल ढूंढने का फंक्शन ---
def get_best_match(user_query):
    if not user_query:
        return None
    # यूजर के सवाल को भी वेक्टर में बदलें
    query_vector = vectorizer.transform([user_query])
    # Cosine Similarity निकालें
    similarities = cosine_similarity(query_vector, question_vectors)
    # सबसे ज़्यादा Similarity वाले सवाल का इंडेक्स ढूंढें
    best_match_index = np.argmax(similarities)
    # Similarity स्कोर निकालें
    highest_similarity = similarities[0, best_match_index]

    # अगर Similarity बहुत कम है (जैसे 0.2 से कम), तो समझें कि कोई मैच नहीं मिला
    if highest_similarity < 0.2:
        return None
    else:
        return questions[best_match_index]

# --- Streamlit UI ---
st.title("FAQ Chatbot (Flutter Basics)")

user_input = st.text_input("Ask a question about Flutter:")

if user_input:
    best_question = get_best_match(user_input)
    if best_question:
        st.write("**Best Matching Question:**", best_question)
        st.write("**Answer:**", faqs[best_question])
    else:
        st.write("Sorry, I don't have an answer for that. Please try asking differently.")