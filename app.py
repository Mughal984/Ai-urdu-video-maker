
import asyncio
import streamlit as st
import edge_tts

st.set_page_config(
    page_title="AI Urdu Video Creator",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 AI Urdu Video Creator")
st.write("Create Urdu voiceovers for your promotional videos.")

text = st.text_area(
    "Apna text yahan likhein",
    placeholder="Yahan apni Urdu kahani ya video script likhein..."
)

voice = st.selectbox(
    "Urdu Voice Select Karein",
    [
        "ur-PK-UzmaNeural",
        "ur-PK-AsadNeural"
    ]
)

async def generate_voice(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("urdu_voice.mp3")

if st.button("🎙️ Generate Urdu Voice"):
    if text.strip():
        with st.spinner("Voice ban rahi hai..."):
            try:
                asyncio.run(generate_voice(text, voice))
                with open("urdu_voice.mp3", "rb") as audio:
                    audio_data = audio.read()

                st.audio(audio_data, format="audio/mp3")
                st.download_button(
                    "Download Urdu Voice",
                    data=audio_data,
                    file_name="urdu_voice.mp3",
                    mime="audio/mpeg"
                )
                st.success("Urdu voice tayyar hai!")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle apna text likhein.")
