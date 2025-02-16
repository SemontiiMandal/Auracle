import streamlit as st
import random

# Simulated AI music generation based on mood
def generate_music(mood):
    music_tracks = {
        "Happy": ["Upbeat Symphony", "Sunshine Groove", "Joyful Beats"],
        "Calm": ["Soothing Waves", "Peaceful Piano", "Tranquil Strings"],
        "Sad": ["Mellow Blues", "Emo Ballad", "Deep Reflections"],
        "Excited": ["Epic Build-Up", "Hyped EDM", "Power Surge"]
    }
    return random.choice(music_tracks.get(mood, ["Default Track"]))

# Initialize session state for song requests if not already present
if "song_requests" not in st.session_state:
    st.session_state["song_requests"] = []

def show():
    st.title("🎵 Song Request Tracker")

    tab1, tab2 = st.tabs(["📝 Song Requests", "🎼 Music Generator"])

    with tab1:
        st.subheader("Track Song Requests")
        song_name = st.text_input("Enter a song request:")
        if st.button("Add Request"):
            if song_name:
                st.session_state["song_requests"].append(song_name)
                st.success(f'Added "{song_name}" to the request list!')
            else:
                st.warning("Please enter a song name before adding.")

        st.subheader("Requested Songs:")
        if st.session_state["song_requests"]:
            for song in st.session_state["song_requests"]:
                st.write(f"- {song}")
        else:
            st.write("No requests yet. Start adding!")

    with tab2:
        st.subheader("AI-Generated Music")
        mood = st.selectbox("Select your mood:", ["Happy", "Calm", "Sad", "Excited"])
        if st.button("Generate Music"):
            music_track = generate_music(mood)
            st.write(f"**Generated Track: {music_track}** 🎶")
