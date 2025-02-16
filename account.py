import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import json
import requests

# Firebase credentials and initialization
if not firebase_admin._apps:
    cred = credentials.Certificate('makeuoft-c360d-f1b19351d4c8.json')
    firebase_admin.initialize_app(cred)

# Helper function to check authentication
def is_authenticated():
    return st.session_state.get("signedout", False)

def app():
    st.title('Welcome to :violet[Pondering] :sunglasses:')

    # Initialize session state variables
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False

    def sign_in_with_email_and_password(email, password):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        try:
            payload = json.dumps({
                "email": email,
                "password": password,
                "returnSecureToken": True
            })
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            r.raise_for_status()  # Check for HTTP errors
            data = r.json()
            st.session_state["signedout"] = True
            st.session_state["username"] = data.get('displayName', email)
            st.session_state["useremail"] = data['email']
            return True
        except requests.exceptions.RequestException as e:
            st.warning(f"Signin failed: {e}")
            return False

    if not is_authenticated():
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            if sign_in_with_email_and_password(email, password):
                st.experimental_rerun()  # Reload the app after successful login
    else:
        st.text(f'Welcome, {st.session_state["username"]}')
        if st.button('Sign out'):
            st.session_state.clear()  # Clear session and log out
            st.experimental_rerun()
