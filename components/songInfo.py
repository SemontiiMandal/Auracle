import streamlit as st
import os

def show():
    st.title("🎵 Song Information")  # Showing the basic title

    # Voice recording instructions and button
    st.subheader("Record your voice")
    st.write("Record your voice to AI generate music based on your description.")
    st.write("Go to the following website: ")
    st.markdown('<a href="https://resonaterecordings.com/voice-recorder/" target="_blank">Click here to open the voice recorder</a>', unsafe_allow_html=True)

    # Handle audio URL and play it
    if "audio_url" in st.session_state:
        st.audio(st.session_state["audio_url"], format="audio/wav")
        st.success("Audio recording ready to play!")

    # Upload your own WAV file
    st.subheader("Upload Your Own WAV")
    uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])
    
    if uploaded_file is not None:
        # Save the uploaded file to session state for playback
        st.session_state["current_song"] = uploaded_file
        st.session_state["audio_progress"] = 0
        st.session_state["audio_playing"] = False
        
        # Save the file temporarily on disk for playback
        save_path = os.path.join("uploaded_audio.wav")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success("Custom track uploaded!")
        
        # Play the uploaded file, using it as an audio player
        st.audio(save_path, format="audio/wav")

# Run the Streamlit app
if __name__ == "__main__":
    show()
