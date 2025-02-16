import streamlit as st
import pandas as pd
import numpy as np 

def show():
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
