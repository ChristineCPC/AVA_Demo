import streamlit as st

#Initializes session state if its not there
if "page" not in st.session_state:
    st.session_state.page = "menu"

def switch_page(page_name):
    st.session_state.page = page_name
    #st.write(f"DEBUG: Switching to {page}")
    st.rerun()

st.set_page_config(page_title = "AVA - AI Vetrainarian  Assistant for Livestock", layout = "wide")

#Customization
st.markdown(
    
    """
        <style>
            body
            {
                background-color: #f4f4f4; /* hex code for light gray*/
            }

            .main
            {
                background-color: white;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
            }

            .stButton button
            {
                width: 100%;
                border-radius: 10px;
                padding: 10px;
                font-size: 10px;
                font-weight: bold;
                background-color: #4CAF50; /*hex code for green*/
                color: white;
                border: none;
            }

            .stButton button: hover
            {
                background-color: #45a049;
            }

        </style>
    """,
    unsafe_allow_html = True
)

st.write(f"DEBUG: Current page - {st.session_state.page}") 

#Home page/Main menu
if st.session_state.page == "menu":
    #Greet user when app is opened
    st.title("Welcome to AVA")
    st.write("Your AI-powered livestock health assistant")
    st.subheader("Select an option below:")

    #Home page buttons
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        if st.button("Get a Diagnosis"):
            switch_page("chatbot")
    with col2:
        if st.button("Chat History"):
            switch_page("chat_history")
    with col3:
        if st.button("Animials"):
            switch_page("view_animals")
    with col4:
        if st.button("Vets Near You"):
            switch_page("vet_finder")
    with col5:
        if st.button("Tasks"):
            switch_page("tasks")
    with col6:
        if st.button("News"):
            switch_page("news")
    with col7:
        if st.button("Settings"):
            switch_page("settings")
    
#Other pages; these will display once the user selects a button
elif st.session_state.page == "chatbot":
    from pages.chatbot import show_diagnosis
    show_diagnosis()   
elif st.session_state.page == "chat_history":
    from pages.chat_history import show_chat_history
    show_chat_history()
elif st.session_state.page == "view_animals":
    from pages.view_animals import show_view_animals
    show_view_animals()
elif st.session_state.page == "vet_finder":
    from pages.vet_finder import show_vet_finder
    show_vet_finder()
elif st.session_state.page == "tasks":
    from pages.tasks import show_tasks
    show_tasks()
elif st.session_state.page == "news":
    from pages.news import show_news
    show_news()
elif st.session_state.page == "settings":
    from pages.settings import show_settings
    show_settings()