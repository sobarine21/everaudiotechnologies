import streamlit as st
import speech_recognition as sr
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="YOUR_API_KEY")

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

def analyze_text_with_gemini(text):
    prompt = f"Analyze the following text: {text}. Provide a summary, identify key points, and suggest potential insights or actions."
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Streamlit app
st.title("Audio Transcription and AI Analysis")
uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    transcript = transcribe_audio("temp_audio.wav")
    st.write("Transcript:")
    st.write(transcript)

    analysis_result = analyze_text_with_gemini(transcript)
    st.write("AI Analysis:")
    st.write(analysis_result)
