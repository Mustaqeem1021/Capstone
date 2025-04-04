import streamlit as st
import requests
import json
import pyperclip


# Function to translate using Deep Translate API
def translate_text(text, target_lang="hi"):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = json.dumps({
        "q": text,
        "source": "en",
        "target": target_lang
    })

    headers = {
        "content-type": "application/json",
        "x-rapidapi-key": "e7c50e818cmshc03308b6c41b724p1f9fcejsn6752e033dbba",  # Replace if needed
        "x-rapidapi-host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        translated = response.json()["data"]["translations"]["translatedText"]
        return translated
    else:
        st.error(f"Translation failed: {response.status_code} - {response.text}")
        return None

# Streamlit UI
st.set_page_config(page_title="English to Hindi Translator", page_icon="🌐")

st.title("🌐 Language Translator")
st.write("Enter your English sentence and get the Hindi translation using Deep Translate API.")

text_input = st.text_area("✏️ Enter English sentence", height=150)

if st.button("Translate"):
    if text_input.strip():
        with st.spinner("Translating..."):
            translated = translate_text(text_input)
            if translated:
                st.success("✅ Translation Complete:")
                st.text_area("📘 Hindi Translation", value=translated, height=150)
    else:
        st.warning("Please enter a sentence to translate.")
