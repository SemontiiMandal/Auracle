import streamlit as st
from components import navbar, happiness_show, history_show, about_show

# Load navbar
page = navbar()

# Display selected page
if page == "Happiness":
    happiness_show()
elif page == "History":
    history_show()
elif page == "About":
    about_show()
