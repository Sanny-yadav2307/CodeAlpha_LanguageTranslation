import streamlit as st
import requests
from gtts import gTTS
import io

# Page Configuration ⚙️️
st.set_page_config(page_title="AI Language Translator", page_icon="🌐", layout="wide")

# Custom Styling (Modern UI) 🎨
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 2em;
        width: 100%;
        border: none;
    }
    .stButton>button:hover { background-color: #45a049; }
    .title-box {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 20px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section 🎯
st.markdown("""
    <div class="title-box">
        <h1>🌐 Modern Language Translator</h1>
        <p>Fast, efficient translation across major global languages!</p>
    </div>
""", unsafe_allow_html=True)

# Language Dictionary 🌍
LANGUAGES = {
    "Hindi": "hi",
    "Bhojpuri": "bho",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
    "Urdu": "ur",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
    "Punjabi": "pa"
}

# Layout: 2 Columns 📐
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input Text")
    user_text = st.text_area("Enter text here:", value="Namaste! Welcome to CodeAlpha internship.", height=180)

with col2:
    st.subheader("🎯 Target Language")
    selected_lang = st.selectbox("Choose language:", list(LANGUAGES.keys()), index=0)
    target_code = LANGUAGES[selected_lang]

# Action Button 🚀
if st.button("🚀 Translate Now"):
    if user_text.strip():
        try:
            # Direct API Request (No rate-limit issues) ⚡
            url = f"https://api.mymemory.translated.net/get?q={user_text}&langpair=autodetect|{target_code}"
            response = requests.get(url)
            data = response.json()
            
            translated_result = data['responseData']['translatedText']
            
            st.markdown("---")
            st.success(f"✅ Translated to **{selected_lang}**:")
            
            # 📋 Copy Feature
            st.code(translated_result, language=None)
            
            # 🔊 Text-To-Speech Feature (Audio Player)
            try:
                tts = gTTS(text=translated_result, lang=target_code)
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                
                st.write("🔊 **Listen Translation:**")
                st.audio(fp, format='audio/mp3')
            except Exception:
                st.info("💡 Audio preview is not available for this language code.")
                
        except Exception as e:
            st.error(f"⚠️ Translation Error: {e}")
    else:
        st.warning("⚠️ Kripya pehle text box me kuch type karein!")

# Command For Code Running: (python -m streamlit run app.py)