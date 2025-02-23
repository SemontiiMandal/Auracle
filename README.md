# Auracle: Music at Your Command

## Introduction

We are excited to introduce **Auracle**, a revolutionary wearable system that brings music control and generation to your fingertips—literally!

Auracle was developed as part of MakeUofT 2025, a Major League Hacking (MLH) hackathon. It was built as a group project by a team of four members over an intense 24-hour development period. 🤝💡

## 🏆 Achievements
Winner of the MLH 'Best Use of Gen AI' Prize at MakeUofT 2025! 🏅🚀

---

## Imagine This:

It’s a freezing winter evening, and you're commuting home. Like every Gen Z, you're plugged into your music—crossing streets, zoning into your favorite track, lost in your world of sound. But there's a problem.

**You're wearing gloves.**  
You can't pull out your phone to skip tracks. You can't search for new music without freezing your fingers. Frustrating, right?

Not anymore.

Introducing **Auracle**—a wearable system that lets you control and generate music using just your voice and gestures—all without taking your hands out of your pockets.

---

## How It Works

- **The Glasses:** Equipped with a voice recording module, the glasses capture your request—whether it’s “play something calming” or “generate an upbeat lofi track.”
- **Speech-to-Music AI:** The audio prompt is converted to text (via Hugging Face’s model) and passed into a Generative AI Music Model, which crafts a completely unique track based on your mood and request.
- **The Gloves:** Featuring an accelerometer-gyroscope sensor, the gloves let you interact with the music effortlessly:

  - **Tilt Right:** Regenerate the music.
  - **Tilt Left:** Stop the track.
  - **Tilt Up:** Increase volume.
  - **Tilt Down:** Decrease volume.

- **The Experience:** The generated music plays through the built-in speaker in the glasses, ensuring a seamless, immersive experience—no phone needed.

- **Online User Interface/Full Stack App:** The user interface is built with Streamlit and Gradio, and the backend is powered by Firebase. User data, including login information and listening moods, is stored and managed through the app. Users can input their voice messages via the website as well, which are processed by the application.

And the best part? You can regenerate the track endlessly until it perfectly matches your vibe.

---
## My Contributions

### My Role:
I worked primarily on the **software side** of the project, contributing the following key components:

1. **Speech-to-Text Model** using HuggingFace:
   - Convert spoken commands into text, allowing users to control the music via voice input.

2. **Generative AI Music Generator** using HuggingFace’s AudioLDM 2:
   - Generate music based on user prompts, making each track unique and tailored to the user’s request.

3. **Text Sentiment Analysis** using TextBlob:
   - Sentiment analysis model that detects the emotional tone of user input and sends that data to a realtime database (Firebase) and user's mood history is logged onto the web app.

4. **Frontend Development with Gradio**:
   - Designed Gradio frontends for each AI model, enabling users to interact with them directly for demonstration purposes during hackathon.

---

## Installation Guide for AI Music Generation 

To run this project, you will need access to a **GPU**. We recommend using **Google Colab** to run the models. Follow these steps:

1. Open the [Google Colab Notebook](<https://colab.research.google.com/drive/1xgslfFNHP8zBEcMYCUEm-MTWyNT89dnB?usp=sharing>) containing the installation and usage instructions.
2. Go to Runtime > Change runtime type > Hardware Accelerator > select a GPU > Click Save
3. Click on Runtime > Run All to start generating music based on your voice input and sentiment analysis; It might take around 5 mins to execute all cells. After the execution, you will be able to access the gradio frontend, using a live link generated which will be shown in the last cell.

**Note:** 
My other two notebooks, SpeechtoText.ipynb and TextSentimentAnalysis.ipynb won't need a GPU to run.

Here are the Colab Notebooks:
1. [Speech to Text Notebook] (<https://colab.research.google.com/drive/14u8gVqNKe6CaNpH9aTBWLG48sOmCwmxn?usp=sharing>)
2. [Text Sentiment Analysis Notebook] (<https://colab.research.google.com/drive/1dp02dyOfmBp_ZZiiMEwgenU_IkJyDfqL?usp=sharing>)

---

## Why AI-Generated Music?

Traditional music platforms like Spotify recommend songs based on your past preferences, keeping you in a loop of similar tracks. But studies show that:

- People experience “playlist fatigue”—constantly searching for new songs is exhausting.
- AI-generated music is hyper-personalized—you get exactly what you ask for.
- Unlike Spotify, **Auracle** is free!

And as we expand, we plan to take it even further.

---

## Why a Website?

We wanted a centralized platform where users could:

- Track their prompt history
- Replay previously generated music
- Visualize their mood trends over time

Think of it as a personalized, AI-powered Spotify—but without the price tag.

**Auracle** isn’t just another music player—it’s the future of music interaction.

🎶 **Voice-controlled. Gesture-enabled. AI-generated.** 🎶

---

Thank you for checking out **Auracle**! 🚀
