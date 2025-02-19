# Auracle: Music at Your Command

## Introduction

Music has been a form of entertainment for many centuries, from the ancient Egyptians to the present day. It has transcended cultures and time, evolving alongside humanity. Early evidence of making music can be traced back to primitive tools and instruments, marking the beginning of human expression through sound. Today, music is celebrated as both an art form and a powerful tool, especially in modern science, such as music therapy.

Therefore, we are excited to introduce **Auracle**, a revolutionary wearable system that brings music control and generation to your fingertips—literally!

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

- **Online User Interface/Full Stack App:** The user interface is built with Streamlit, and the backend is powered by Firebase. User data, including login information and listening moods, is stored and managed through the app. Users can input their voice messages via the website as well, which are processed by the application.

And the best part? You can regenerate the track endlessly until it perfectly matches your vibe.

---

## Challenges We Overcame

Like any ambitious project, **Auracle** faced several obstacles:

1. **ESP32 Module Unavailability:** We initially planned to use an ESP32 module to transfer data between our recorder and speaker. However, hardware constraints forced us to pivot to an ESP32-CAM module, which turned out to be defective. Despite reaching out to tech support, the issue remained unresolved. As a result, we had to simulate sensor data instead.

2. **Speaker but No Recorder:** While we acquired a speaker module, we couldn’t get a compatible voice recorder in time. Currently, we’re simulating voice input via a laptop microphone.

3. **Stretch Sensor Shortages:** Our initial design included stretch sensors for finer gesture detection, but due to stock shortages, we adapted by relying on gyroscope-based gestures instead.

Despite these setbacks, **Auracle** is functional—and more importantly, it lays the groundwork for an entirely new way of interacting with music.

---

## Why AI-Generated Music?

Traditional music platforms like Spotify recommend songs based on your past preferences, keeping you in a loop of similar tracks. But studies show that:

- People experience “playlist fatigue”—constantly searching for new songs is exhausting.
- AI-generated music is hyper-personalized—you get exactly what you ask for.
- Unlike Spotify, **Auracle** is free!

And as we expand, we plan to take it even further.

---

## Future Scope

- **Personalized Mood Dashboard:** We plan to introduce an ML model that tracks user prompt history to analyze mood trends over time. This could help identify mood swings, which are early indicators of stress, burnout, and mental health conditions.

- **Expanding Beyond Music:** Imagine using **Auracle** to generate customized ambient sounds for sleep, meditation, or focus—tailored to your emotional state.

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
