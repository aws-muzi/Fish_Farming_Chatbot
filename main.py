import streamlit as st

from streamlit_option_menu import option_menu
import about, account, home, chatbot, your_posts
from datetime import datetime

st.set_page_config(
    page_title="Fish Farming",
    initial_sidebar_state = "auto",
)
st.write("", unsafe_allow_html=True)

# Link to your external CSS file
# st.sidebar.markdown("""<link rel="stylesheet" href="style.css">""", unsafe_allow_html=True)

# menu_title_color = "yellow"  # Replace with your desired color code
# menu_title_font_size = "10px"  # Replace with your desired font size

class MultiApp:
    
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        
        with st.sidebar:
            app = option_menu(
                menu_title='Fish Farming',
                options=[ 'Account', 'About','Forum','Your Posts','ask-a-bot'],
                icons=['person-square', 'exclamation-square','house-fill', 'trophy-fill','chat-text-fill'],
                menu_icon='None',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":"#00d8bf"},  #61AEA6
                    "icon": {"color": "white", "font-size": "20px"}, 
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#90e0ef"},  #a1e3dc
                    "nav-link-selected": {"background-color": "#1a725f"},  #1A7269
                }
        
            )
            
        if app == "Forum":
            home.app()
        if app == "Account":
            account.app()
            st.session_state["sidebar_visible"] = False
        if app == 'About':
            about.app()
        if app == 'Your Posts':
            your_posts.app()           
        if app == 'ask-a-bot':
            chatbot.app()
            
    run()

    def my_t():
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    last_update = None
    
    while True:
        now = datetime.now()
        if last_update is None or (now - last_update).total_seconds() >= 1:
            st.write("Current Time: ", my_t())
            last_update = now
        st.empty()


    

