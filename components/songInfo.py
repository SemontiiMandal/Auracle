import streamlit as st
import random
import time

# Simulated AI music generation based on mood
def generate_music(mood):
    music_tracks = {
        "Happy": ["upbeat_symphony.mp3", "sunshine_groove.mp3", "joyful_beats.mp3"],
        "Calm": ["soothing_waves.mp3", "peaceful_piano.mp3", "tranquil_strings.mp3"],
        "Sad": ["mellow_blues.mp3", "emo_ballad.mp3", "deep_reflections.mp3"],
        "Excited": ["epic_build_up.mp3", "hyped_edm.mp3", "power_surge.mp3"]
    }
    return random.choice(music_tracks.get(mood, ["default_track.mp3"]))

# Initialize session state
if "song_requests" not in st.session_state:
    st.session_state["song_requests"] = []
if "current_song" not in st.session_state:
    st.session_state["current_song"] = None
if "audio_playing" not in st.session_state:
    st.session_state["audio_playing"] = False
if "audio_progress" not in st.session_state:
    st.session_state["audio_progress"] = 0

def show():
    st.title("🎵 Song Information")  # Showing the basic title
    tab1, tab2 = st.tabs(["📝 Song Requests", "🎼 Music Generator"])  # Creating two tabs

    # Tab 1: Song Requests
    with tab1:
        st.subheader("Track Song Requests")
        song_name = st.text_input("Enter a song request:")
        
        if st.button("Add Request"):
            if song_name:
                st.session_state["song_requests"] = st.session_state["song_requests"] + [song_name]
                st.success(f'Added "{song_name}" to the request list!')
            else:
                st.warning("Please enter a song name before adding.")

        st.subheader("Requested Songs:")
        if st.session_state["song_requests"]:
            for song in st.session_state["song_requests"]:
                st.write(f"- {song}")
        else:
            st.write("No requests yet. Start adding!")

    # Tab 2: AI Music Generator & Audio Player
    with tab2:
        st.subheader("AI-Generated Music")
        mood = st.selectbox("Select your mood:", ["Happy", "Calm", "Sad", "Excited"])
        
        if st.button("Generate Music"):
            st.session_state["current_song"] = generate_music(mood)
            st.session_state["audio_progress"] = 0
            st.session_state["audio_playing"] = False
            st.success(f"Generated track: {st.session_state['current_song']} 🎶")

        # Upload your own MP3 file
        st.subheader("Upload Your Own MP3")
        uploaded_file = st.file_uploader("Choose an MP3 file", type=["mp3"])
        if uploaded_file is not None:
            st.session_state["current_song"] = uploaded_file
            st.session_state["audio_progress"] = 0
            st.session_state["audio_playing"] = False
            st.success("Custom track uploaded!")
        
        st.markdown(
            """
            <style> 
                .button-container {
                    display: flex; 
                    gap: 10px; 
                    margin-top: 10px; 
                }
                .music-button {
                    padding: 10px 20px; 
                    font-size: 16px; 
                    border: none; 
                    border-radius: 5px; 
                    cursor: pointer;
                }
            </style>

            <div class="button-container">
                <button class="music-button play" onclick="playAudio()">▶ Play</button>
                <button class="music-button pause" onclick="pauseAudio()">⏸ Pause</button>
            </div>

            """,
            unsafe_allow_html=True


        )

       

# Run the Streamlit app
if __name__ == "__main__":
    show()
