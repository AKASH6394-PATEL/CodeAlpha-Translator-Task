import streamlit as st
# deep_translator को import किया
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

# Streamlit ऐप का टाइटल
st.title("Simple Language Translator by Akash")

# टेक्स्ट इनपुट लेने के लिए बॉक्स
text_to_translate = st.text_area("Enter text to translate:", height=150)

# भाषाओं की लिस्ट बनाएं (Google Translate के लिए)
# Name: Code format
language_options = {name: code for code, name in GOOGLE_LANGUAGES_TO_CODES.items()}
language_names = sorted(list(language_options.keys())) # नामों को Alphabetically Sort करें

# Source और Target भाषा चुनने के लिए ड्रॉपडाउन
col1, col2 = st.columns(2)
with col1:
    # Default में English चुनें
    try:
        eng_index = language_names.index('english')
    except ValueError:
        eng_index = 0 # Fallback
    source_lang_name = st.selectbox("From Language:", language_names, index=eng_index)
    source_lang_code = language_options[source_lang_name] # नाम से कोड निकालें

with col2:
    # Default में Hindi चुनें
    try:
        hin_index = language_names.index('hindi')
    except ValueError:
        hin_index = 0 # Fallback
    target_lang_name = st.selectbox("To Language:", language_names, index=hin_index)
    target_lang_code = language_options[target_lang_name] # नाम से कोड निकालें

# ट्रांसलेट बटन
if st.button("Translate"):
    if text_to_translate:
        try:
            # ट्रांसलेशन करें (GoogleTranslator का इस्तेमाल करके)
            st.spinner("Translating...")
            translated = GoogleTranslator(source=source_lang_code, target=target_lang_code).translate(text_to_translate)

            # ट्रांसलेटेड टेक्स्ट दिखाएं
            st.subheader("Translated Text:")
            st.write(translated)
        except Exception as e:
            st.error(f"An error occurred during translation: {e}")
            st.error("Please check your internet connection or try again.")
    else:
        st.warning("Please enter some text to translate.")