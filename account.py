import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import requests

# Firebase credentials and initialization
if not firebase_admin._apps:
    cred = credentials.Certificate('/Users/averylor/Desktop/makeUofT/emotionalDamage/makeuoft-c360d-b816b64042f8.json')
    firebase_admin.initialize_app(cred)

# Helper function to check authentication
def is_authenticated():
    return st.session_state.get("signedout", False)

# Function to create an account
def create_account(email, password):
    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
    try:
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, json=payload)
        r.raise_for_status()
        st.success("Account created successfully! Please log in.")
        return True
    except requests.exceptions.RequestException as e:
        error_message = r.json().get("error", {}).get("message", "Unknown error")
        st.warning(f"Signup failed: {error_message}")
        return False

# Function to sign in
def sign_in_with_email_and_password(email, password):
    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
    try:
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, json=payload)
        r.raise_for_status()
        data = r.json()
        st.session_state["signedout"] = True
        st.session_state["username"] = data.get('displayName', email)
        st.session_state["useremail"] = data['email']
        return True
    except requests.exceptions.RequestException as e:
        error_message = r.json().get("error", {}).get("message", "Unknown error")
        st.warning(f"Signin failed: {error_message}")
        return False

def app():
    st.title('Auracle Login Page 🌟')

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False

    if not is_authenticated():
        choice = st.radio("Choose an option:", ["Login", "Create Account"])

        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if choice == "Create Account":
            if st.button("Sign Up"):
                if create_account(email, password):
                    st.rerun()
        else:  # Login options
            if st.button("Login"):
                if sign_in_with_email_and_password(email, password):
                    st.rerun()
    else:
        if st.button('Sign out'):
            st.session_state.clear()
            st.rerun()
