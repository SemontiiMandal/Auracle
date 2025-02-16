import streamlit as st
from components import navbar, happiness_show, history_show, about_show
import account

# Load navbar
page = navbar()

# Display selected page
if page == "Happiness":
    happiness_show()
elif page == "History":
    history_show()
elif page == "Account":
    account.app()
elif page == "About":
    about_show()
