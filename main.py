import streamlit as st

from streamlit_option_menu import option_menu
import about, account, home, chatbot, your_posts

st.set_page_config(
    page_title="Fish Farming",
    initial_sidebar_state = "expanded",
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
                    "container": {"padding": "5!important"},  #61AEA6
                    "icon": {"color": "#1a725f", "font-size": "20px"}, 
                    "nav-link": {"color":"#1a725f","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "yellow"},  #a1e3dc
                    "nav-link-selected": {"background-color": "#1a725f","color":"white"},  #1A7269
                    }
        
                )
            notepad = st.checkbox(":orange[write notes]")
            if notepad:
                # Text area for user to enter notes
                notes = st.text_area("Take your notes here:")

                # Text input for filename
                filename = st.text_input("Enter a filename for your notes:", "your_notes.txt")

                # Function to generate a text file from notes
                def get_text_file(notes):
                    # Convert the notes to bytes
                    return notes.encode('utf-8')

                # Display the save button and download button conditionally
                if st.button("Save Notes"):
                    # Call the function to get text file
                    tmp_file = get_text_file(notes)
                    # Check if filename has .txt extension, add if not
                    if not filename.endswith('.txt'):
                        filename += '.txt'
                    # Create download button for the text file
                    st.download_button(
                        label="Download Notes",
                        data=tmp_file,
                        file_name=filename,
                        mime="text/plain",
                        help="Click to download your notes as a TXT file."
                    )    
            
        if app == "Forum":
            home.app()
        if app == "Account":
            account.app()
        if app == 'About':
            about.app()
        if app == 'Your Posts':
            your_posts.app()
        if app == 'ask-a-bot':
            chatbot.app()
    
    run()
