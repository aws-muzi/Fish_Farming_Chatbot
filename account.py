import  streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import time


cred = credentials.Certificate("fish-farming-chatbot-c20b971ecafc.json")
firebase_admin.initialize_app(cred)

def app():
    
    
  #  choice = st.selectbox('Login or Signup', ['Login', 'Sign Up'])
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
        
    
    def f():
        try:
            user = auth.get_user_by_email(email)
            #print(user.uid)
            
            progress_bar = st.progress(0)              
            
            for perc_completed in range(100):
                time.sleep(0.05)
                progress_bar.progress(perc_completed + 1)
            st.success('Login Successful')
            st.balloons()
            time.sleep(0.02)
            progress_bar.empty()
            
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            st.session_state.signout = True
            st.session_state.signedout = True
            
        except:
            st.warning('Login Failed')
    
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
        
            
    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False
        
    if not st.session_state['signedout']:
        st.title(" Welcome to the :orange[Fish Farming Chatbot]")
        choice = st.selectbox('Login or Signup', ['Login', 'Sign Up'])
    
        if choice == 'Login':
            
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            
            st.button('Login', on_click = f)
            
        else:
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            password2 = st.text_input('Confirm Password', type='password')
            username = st.text_input('Enter your username')
            
            if st.button('Create an account'):
                user = auth.create_user(email = email, password = password, uid = username)
                
                st.success('Your account has been successfully created!')
                st.success('You may login using your email and password')
                st.balloons()
                
                
    if st.session_state.signout:
        st.title(" Welcome " + ':orange[' + st.session_state.username + ']')
        st.text('UserName: ' + st.session_state.username)
        st.text('Email ID: ' + st.session_state.useremail)
        st.button('Sign out', on_click= t)
        
        st.image("happy.gif")
        
