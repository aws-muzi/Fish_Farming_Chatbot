import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from extra_streamlit_components import st_text_input, st_button
import time

cred = credentials.Certificate("fish-farming-chatbot-c20b971ecafc.json")
firebase_admin.initialize_app(cred)

def app():

    # Session state variables (with expiry)
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'last_active' not in st.session_state:
        st.session_state.last_active = time.time()  # Initialize timestamp

    # Function to check session expiry (customizable expiry time in seconds)
    def is_session_expired(expiry_time=120):  # Adjust expiry_time as needed (e.g., 300 for 5 mins)
        return time.time() - st.session_state.last_active > expiry_time

    # Login function with progress bar and session update
    def login():
        try:
            email = email_input.text
            password = password_input.text

            progress_bar = st.progress(0)

            for perc_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(perc_completed + 1)

            user = auth.get_user_by_email(email)

            st.success('Login Successful')
            st.balloons()
            time.sleep(0.02)
            progress_bar.empty()

            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.last_active = time.time()  # Update last activity

            st.session_state.signout = True
            st.session_state.signedout = False

        except:
            st.warning('Login Failed')

    # Sign out function and session reset
    def signout():
        st.session_state.signout = False
        st.session_state.signedout = True
        st.session_state.username = ''
        st.session_state.useremail = ''

    # Main app logic
    if not st.session_state.signedout and not is_session_expired():
        st.title("Welcome to the :orange[Fish Farming Chatbot]")
        choice = st.selectbox('Login or Signup', ['Login', 'Sign Up'])

        if choice == 'Login':
            email_input = st.text_input('Email Address')
            password_input = st.text_input('Password', type='password')

            st.button('Login', on_click=login)

        else:
            # Sign Up functionality (omitted for brevity)

    # Display logged-in user information and sign out button
    if st.session_state.signout and not is_session_expired():
        st.title("Welcome " + ':orange[' + st.session_state.username + ']')
        st.text('UserName: ' + st.session_state.username)
        st.text('Email ID: ' + st.session_state.useremail)
        st.button('Sign out', on_click=signout)
        st.image("happy.gif")

    # Refresh session timer on any user interaction
    if not is_session_expired():
        st.session_state.last_active = time.time()

if __name__ == "__main__":
    app()
