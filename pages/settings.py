import streamlit as st

def show_settings():
    st.title("Settings")
    st.write("Customize your user experience.")

    theme = st.radio("Choose a theme:", ["Light Mode", "Dark Mode", "Default"])
    notifications = st.selectbox("Allow push-notifications:", ["Enable", "Disable"])

    if st.button("Save Preferences"):
        st.success("Saved!")


    #Takes user back to the home screen
    if st.button("Main Menu"):
        st.session_state.page = "menu"
        st.rerun()