import streamlit as st
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key =  os.getenv("OPENAI_API_KEY")

#enter symptoms to Deepseek to get a diagnosis
def get_diagnosis(symptoms):
  #connects to deepseek and tells AI what to do

    client = OpenAI(base_url = "https://openrouter.ai/api/v1", api_key = openai_api_key)
    #try:
    completion = client.chat.completions.create(
        #extra_body={}
        model = "deepseek/deepseek-r1:free",
        messages = [
            {
                "role":"system",
                "content":"You are a medical diagnosis assistant specialized in livestock diseases. Based on the given symptoms, provide a possible diagnosis and suggest next steps."
            },
            {
                "role":"user",
                "content":f"Here are the symptoms: {symptoms}"
            }
        ]
    )
    return completion.choices[0].message.content.strip()

    #except Exception as e:
        #return f"Error: {str(e)}"


#UI
def show_diagnosis():
    st.title("Get a Diagnosis")
    st.write("Enter symptoms below to get a preliminary diagnosis for your animal.")

    #input field
    symptoms = st.text_area("Describe the symptoms:")
    if st.button("Submit"):
        if symptoms:
            diagnosis = get_diagnosis(symptoms)
            st.header("Possible Diagnosis:")
            st.write(diagnosis)
        else:
            st.warning("Please enter symptoms before proceeding.")

    #Takes user back to the home screen
    if st.button("Main Menu"):
        st.session_state.page = "menu"
        st.rerun()

'''
#List of exxamples of vets, use a database for actual implentation
vet_list = ["Dr.Smith - Texas Livestock Care", "Dr.Burns - Farm Animal Hospital"] 
for vet in vet_list:
    st.write(f"- {vet}")
'''

#Disclaimer
st.write("\nNote: ADA's advice does not replace the advice of professonal veterinarians.")
