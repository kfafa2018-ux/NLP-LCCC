import streamlit as st
from textblob import TextBlob
from googletrans import Translator

st.title("Multi-Language Translator & Sentiment Analyzer")
st.write("Translate text to Spanish, German, Mandarin, or French, and analyze sentiments!")

# Language Mapping
language_options = {
    "Spanish": "es",
    "German": "de",
    "Mandarin": "zh-cn",
    "French": "fr"
}

# User Input
user_text = st.text_area("Enter the text you want to translate:", "I love coding in Python, but sometimes it is challenging!")
target_lang = st.selectbox("Select Target Language:", list(language_options.keys()))

if st.button("Translate & Analyze"):
    if user_text.strip() != "":
        # Original Sentiment
        blob_input = TextBlob(user_text)
        sentiment_input = blob_input.sentiment
        
        # Translate using googletrans
        translator = Translator()
        lang_code = language_options[target_lang]
        try:
            translation_result = translator.translate(user_text, dest=lang_code)
            translated_text = translation_result.text
        except Exception as e:
            translated_text = f"Translation failed: {str(e)}"

        # Display Results
        st.subheader("Original Text Sentiment")
        st.write(f"**Polarity:** {sentiment_input.polarity:.2f} (ranges from -1 to 1)")
        st.write(f"**Subjectivity:** {sentiment_input.subjectivity:.2f} (ranges from 0 to 1)")
        
        st.subheader("Translated Text")
        st.write(translated_text)
        
        if "Translation failed" not in translated_text:
            blob_translated = TextBlob(translated_text)
            sentiment_translated = blob_translated.sentiment
            st.subheader("Translated Text Sentiment")
            st.write(f"**Polarity:** {sentiment_translated.polarity:.2f}")
            st.write(f"**Subjectivity:** {sentiment_translated.subjectivity:.2f}")
    else:
        st.warning("Please enter some text to translate.")
