import streamlit as st
import pandas as pd
import numpy as np 
import firebase_admin 

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('emotionalDamage/makeuoft-c360d-679e8029ef77.json')
firebase_admin.initialize_app(cred)


def show():
    st.title("📊 Mood History")

    # Simulate mood data
    dates = pd.date_range(start="2024-04-01", periods=10)
    moods = np.random.choice(["Happy", "Calm", "Sad", "Excited"], size=10)
    df = pd.DataFrame({"Date": dates, "Mood": moods})

    # Chart 
    st.line_chart(df.set_index("Date"))
