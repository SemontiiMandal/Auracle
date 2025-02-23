import gradio as gr

def echo_audio(audio):
    return audio

with gr.Blocks() as demo:
    gr.Markdown("### Gradio Audio Recorder")
    audio_input = gr.Audio(source="microphone", type="filepath")
    output_audio = gr.Audio()
    audio_input.change(echo_audio, inputs=audio_input, outputs=output_audio)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
