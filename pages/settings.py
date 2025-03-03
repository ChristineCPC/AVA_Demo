import streamlit as st

st.title("Settings")
st.write("Customize your user experience.")

theme = st.selectbox("Choose a theme:", ["Light Mode", "Dark Mode", "Default"])
notifications = st.selectbox("Allow push-notifications:", ["Enable", "Disable"])

if st.button("Save Preferences"):
    st.success("Saved!")