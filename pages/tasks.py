import streamlit as st

def show_tasks():
    st.write("coming soon...")

    #Takes user back to the home screen
    if st.button("Main Menu"):
        st.session_state.page = "menu"
        st.rerun()
