import streamlit as st

st.set_page_config(page_title = "ADA - AI Diagnosis Assistant for Livestock")

#Greet user when app is opened
st.title("Welcome to ADA")
st.write("Your AI-powered livestock health assistant")

#Navigation Menu
st.sidebar.title("Navigation")
st.sidebar.page_link("pages/chatbot.py", label = "Get a Diagnosis")
st.sidebar.page_link("pages/chat_history.py", label = "Chat History")
st.sidebar.page_link("pages/view_animals.py", label = "Animals")
st.sidebar.page_link("pages/vet_finder.py", label = "Near by Vets")
st.sidebar.page_link("pages/tasks.py", label = "Tasks")
st.sidebar.page_link("pages/news.py", label = "Tasks")
st.sidebar.page_link("pages/settings.py", label = "Settings")