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
    st.title("🎵 Music Information") # showing the basic title
    tab1, tab2 = st.tabs(["📝 Song Requests", "🎼 Music Generator"]) # creating two tabs for both song request and generating music

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


"""
import random
import torch
import gradio as gr

def create_music(prompt, length_in_seconds):
    # Generate a new random seed each time a user enters a prompt
    seed_value = random.randint(0, 2**32 - 1)
    generator.manual_seed(seed_value)  # Set new seed

    # Generate audio with the new seed
    audio = pipe(prompt, audio_length_in_s=length_in_seconds, num_inference_steps=20,
                 negative_prompt="Low quality, average quality.", generator=generator).audios[0]

    return 16000, audio  # Returning sample rate and generated audio

# Gradio UI
interface = gr.Interface(
    title="Mood-Based Music Generation App 🎵",
    description="Generate music and sounds based on text prompts. Spark your creativity!",
    examples=[
        ["The sound of Brazilian samba drums with waves gently crashing in the background", 10],
        ["Music with dancing unicorns sound", 15]
    ],
    fn=create_music,
    inputs=[
        gr.Textbox(label="Enter a description of the music"),
        gr.Slider(5, 60, step=1, value=10, label="Select Duration (seconds)")
    ],
    outputs="audio",
)

interface.launch(debug=True)
"""