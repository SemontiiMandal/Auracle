import streamlit as st

def show():
    st.title("🎵 Song Information")  # Showing the basic title

    # Voice recording instructions and button
    st.subheader("Record your voice")
    st.write("Record your voice to AI generate music based on your description.")
    
    # Add JavaScript for recording functionality
    st.markdown("""
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
            <button class="music-button" id="start-recording-btn">🎤 Start Recording</button>
            <button class="music-button" id="stop-recording-btn" disabled>⏹ Stop Recording</button>
        </div>

        <script>
            let mediaRecorder;
            let audioChunks = [];
            const startRecordingButton = document.getElementById('start-recording-btn');
            const stopRecordingButton = document.getElementById('stop-recording-btn');
            let audioBlob;

            // Start recording
            startRecordingButton.onclick = async function() {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                mediaRecorder = new MediaRecorder(stream);
                
                mediaRecorder.ondataavailable = function(event) {
                    audioChunks.push(event.data);
                };
                
                mediaRecorder.onstop = function() {
                    audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                    const audioUrl = URL.createObjectURL(audioBlob);
                    const audio = new Audio(audioUrl);
                    audio.controls = true;
                    document.body.appendChild(audio);
                    audio.play();

                    // Pass the audio URL to Streamlit session state
                    window.parent.postMessage({ type: "set_audio_url", audioUrl: audioUrl }, "*");
                };

                mediaRecorder.start();
                startRecordingButton.disabled = true;
                stopRecordingButton.disabled = false;
            };

            // Stop recording
            stopRecordingButton.onclick = function() {
                mediaRecorder.stop();
                startRecordingButton.disabled = false;
                stopRecordingButton.disabled = true;
            };

            // Listen for the message from the Streamlit app to set audio URL in session state
            window.addEventListener("message", function(event) {
                if (event.data.type === "set_audio_url") {
                    // Send the audio URL back to Streamlit using window.parent.postMessage
                    const audioUrl = event.data.audioUrl;
                    window.parent.postMessage({ type: "audio_url", audioUrl: audioUrl }, "*");
                }
            });
        </script>
        """, unsafe_allow_html=True)

    # Handle audio URL and play it
    if "audio_url" in st.session_state:
        st.audio(st.session_state["audio_url"], format="audio/wav")
        st.success("Audio recording ready to play!")

    # Upload your own MP3 file
    st.subheader("Upload Your Own MP3")
    uploaded_file = st.file_uploader("Choose an MP3 file", type=["mp3"])
    if uploaded_file is not None:
        st.session_state["current_song"] = uploaded_file
        st.session_state["audio_progress"] = 0
        st.session_state["audio_playing"] = False
        st.success("Custom track uploaded!")

    # Play/Pause buttons for uploaded or generated music
    st.markdown(
        """
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
