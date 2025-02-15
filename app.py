import streamlit as st
from components import navbar, home_show, about_show, contact_show

# Load navbar
page = navbar()

# Display selected page
if page == "Home":
    home_show()
elif page == "About":
    about_show()
elif page == "Contact":
    contact_show()
