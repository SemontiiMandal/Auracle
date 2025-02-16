import streamlit as st
import pandas as pd
import numpy as np 

def show():
    st.title("📜 Mood History")

    # Simulate mood data
    dates = pd.date_range(start="2024-04-01", periods=10)
    moods = np.random.choice(["Excited", "Happy", "Neutral", "Sad", "Serious Depression"], size=10)
    df = pd.DataFrame({"Date": dates, "Mood": moods})

    # Chart 
    st.line_chart(df.set_index("Date"))
