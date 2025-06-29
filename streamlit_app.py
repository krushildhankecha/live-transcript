# streamlit_app.py
import streamlit as st
from streamlit_audiorecorder import audiorecorder
import whisper

st.set_page_config(page_title="Live Transcription", layout="centered")
st.title("🎙️ Live Audio Transcription")

@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()
audio = audiorecorder("▶️ Start", "⏹️ Stop")

if audio:
    st.audio(audio.export().read(), format="audio/wav")
    with open("user.wav", "wb") as f:
        f.write(audio.export().read())
    st.write("Transcribing...")

    result = model.transcribe("user.wav")
    st.write("📝 Transcript:")
    st.write(result["text"])
