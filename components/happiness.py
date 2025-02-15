import streamlit as st
import random

def generate_music(mood):
    """Simulated AI music generation based on mood."""
    music_tracks = {
        "Happy": ["Upbeat Symphony", "Sunshine Groove", "Joyful Beats"],
        "Calm": ["Soothing Waves", "Peaceful Piano", "Tranquil Strings"],
        "Sad": ["Mellow Blues", "Emo Ballad", "Deep Reflections"],
        "Excited": ["Epic Build-Up", "Hyped EDM", "Power Surge"]
    }
    return random.choice(music_tracks.get(mood, ["Default Track"]))

def show():
    st.title("😊 Happiness & Music Generation")

    tab1, tab2 = st.tabs(["🎭 Mood Tracking", "🎵 Music Generator"])

    with tab1:
        st.subheader("Current Mood Analysis")
        mood = random.choice(["Happy", "Calm", "Sad", "Excited"])
        st.write(f"**Your Detected Mood: {mood}**")

    with tab2:
        st.subheader("AI-Generated Music")
        music_track = generate_music(mood)
        st.write(f"**Generated Track: {music_track}** 🎶")
