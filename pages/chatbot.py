import streamlit as st
import requests
from openai import OpenAI

#enter symptoms to Deepseek to get a diagnosis
def get_diagnosis(symptoms):
  #connects to deepseek and tells AI what to do

    client = OpenAI(base_url = "https://openrouter.ai/api/v1", api_key = "placeholder")
    try:
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

    except Exception as e:
        return f"Error: {str(e)}"

#UI
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

#List of exxamples of vets, use a database for actual implentation
vet_list = ["Dr.Smith - Texas Livestock Care", "Dr.Burns - Farm Animal Hospital"] 
for vet in vet_list:
    st.write(f"- {vet}")

#Disclaimer
st.write("\nNote: ADA's advice does not replace the advice of professonal veterinarians.")
