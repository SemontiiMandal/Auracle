import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests

# Firebase credentials and initialization
cred = credentials.Certificate('path/to/emotionalDamage/makeuoft-c360d-679e8029ef77.json')
firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to :violet[Pondering] :sunglasses:')

    # Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False 

    def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            }
            if username:
                payload["displayName"] = username
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            r.raise_for_status()  # Check for HTTP errors
            return r.json()['email']
        except requests.exceptions.RequestException as e:
            st.warning(f"Signup failed: {e}")
        except Exception as e:
            st.warning(f"Error: {e}")

    def sign_in_with_email_and_password(email, password, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        try:
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            }
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            r.raise_for_status()  # Check for HTTP errors
            data = r.json()
            user_info = {
                'email': data['email'],
                'username': data.get('displayName')  # Retrieve username if available
            }
            return user_info
        except requests.exceptions.RequestException as e:
            st.warning(f"Signin failed: {e}")
        except Exception as e:
            st.warning(f"Error: {e}")

    def reset_password(email):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
            payload = {
                "email": email,
                "requestType": "PASSWORD_RESET"
            }
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            r.raise_for_status()  # Check for HTTP errors
            return True, "Reset email sent"
        except requests.exceptions.RequestException as e:
            return False, f"Error: {e}"
        except Exception as e:
            return False, str(e)

    def handle_login():
        userinfo = sign_in_with_email_and_password(st.session_state.email_input, st.session_state.password_input)
        if userinfo:
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']
            st.session_state.signedout = True
            st.session_state.signout = True

    def handle_signout():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
        st.session_state.useremail = ''

    def forget_password():
        email = st.text_input('Email')
        if st.button('Send Reset Link'):
            success, message = reset_password(email)
            if success:
                st.success(message)
            else:
                st.warning(message)

    if not st.session_state.signedout:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email, password=password, username=username)
                if user:
                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
        else:
            st.button('Login', on_click=handle_login)
            forget_password()

    if st.session_state.signout:
        st.text(f'Name: {st.session_state.username}')
        st.text(f'Email: {st.session_state.useremail}')
        st.button('Sign out', on_click=handle_signout)

    def ap():
        st.write('Posts')
