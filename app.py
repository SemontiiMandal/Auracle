import streamlit as st
from components import navbar, songInfo_show, history_show, about_show
import account

# Ensure authentication before displaying anything else
if not account.is_authenticated():
    account.app()  # Show the login page
else:
    # Load navbar after authentication
    page = navbar()

    # Display selected page
    if page == "Song Info":
        songInfo_show()
    elif page == "History":
        history_show()
    elif page == "Account":
        account.app()
    elif page == "About":
        about_show()
