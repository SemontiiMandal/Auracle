import streamlit as st
import navbar
import home
import contact

# Load navigation bar
page = navbar.navbar()

# Display selected page
if page == "Home":
    home.show()
elif page == "Contact":
    contact.show()
