import streamlit as st
import components.navbar as navbar
import components.home as home
import components.contact as contact

# Load navigation bar
page = navbar.navbar()

# Display selected page
if page == "Home":
    home.show()
elif page == "Contact":
    contact.show()
