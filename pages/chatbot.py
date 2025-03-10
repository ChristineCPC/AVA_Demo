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
    #initializes chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown(

        """
            <style>
                body
                {
                    background-color: #f4f4f4;
                }

                .chat-container
                {
                    background-color: white;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: auto;
                }

                .chat-bubble
                {
                    padding: 10px 15px;
                    border-raduis: 15px;
                    margin: 5px 0;
                    display: inline-block;
                    max-width: 80%;
                    font-size: 16px;
                }

                .user-bubble
                {
                    background-color: #46B4E3; /*light blue*/
                    align-self: flex-end;
                    text-aligh; right;
                }

                .ai-bubble
                {
                    background-color: #696969; /*light grey*/
                    align-self: flex-start;
                }

                .avatar
                {
                    width: 40px;
                    height: 40px;
                    border-raduis: 50%;
                    margin-right: 10px;
                }

                .chat-box
                {
                    display: flex;
                    align-itmes: center;
                    margin-bottom: 10px;
                }

                .header
                {
                    background: linear-gradient(to right, #2226ff, #81c6f7);
                    color: white;
                    padding: 15px;
                    text-align: center;
                    font-size: 100px;
                    border-radius: 10px 10px 0 0;
                }

                .input-continer
                {
                    display: flex;
                    align-items: center;
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                    background: white;
                    padding: 10px;
                    box-shadow: 0px -2px 5px rgba(0,0,0,0.1);
                }

                .input-box
                {
                    flex: 1;
                    padding: 10px;
                    border-raduis: 20px;
                    border: 1px solid #ccc;
                    margin-right: 10px;
                }

                .send-button
                {
                    background-color: #6200EA;
                    color: white;
                    padding: 10px 15px;
                    border: none;
                    border-radius: 20px;
            
                    font-size: 16px
                }

            </style>    
        """,
        unsafe_allow_html = True

    )

    #Header
    st.markdown('<div class ="header"> AVA </div>', unsafe_allow_html = True)

    #Chat Container
    st.markdown('<div class = "chat-container>', unsafe_allow_html = True)

    #shows chat log
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class = "chat-box" style = "justify-content: flex-end;">'
                f'<div class = "chat-bubble user-bubble">{msg["content"]} </div>'
                f'</div>',
                unsafe_allow_html = True
            )
        else:
            st.markdown(
                f'<div class = "chat-box">'
                #f'<img class = "avatar" src = ' add avatar images later
                f'<div class = "chat-bubble ai-bubble"> {msg["content"]}</div>'
                f'</div>',
                unsafe_allow_html = True
            )

    #closes chat container
    st.markdown('</div>', unsafe_allow_html = True)

    symptoms = st.text_input("", key = "chat_input", placeholder = "Describe symptoms...", label_visibility = "hidden")
    send_button = st.button("Send", key = "send_button")

    if send_button and symptoms:
        st.session_state.messages.append({"role": "user", "content": symptoms})
        diagnosis = get_diagnosis(symptoms)
        st.session_state.messages.append({"role": "ai", "content": diagnosis})
        st.rerun()
    elif send_button:
        st.warning("Please enter symptoms before proceeding.")

    #st.title("Get a Diagnosis")
    
    #st.write("Enter symptoms below to get a preliminary diagnosis for your animal.")
    '''
    get rid of this later
    #input field
    symptoms = st.text_area("Describe the symptoms:")
    if st.button("Submit"):
        if symptoms:
            diagnosis = get_diagnosis(symptoms)
            st.header("Possible Diagnosis:")
            st.write(diagnosis)
        else:
            st.warning("Please enter symptoms before proceeding.")

    '''
    #Takes user back to the home screen and clears the chat
    if st.button("Main Menu"):
        st.session_state.page = "menu"
        st.session_state.messages = []
        st.rerun()

'''
#List of exxamples of vets, use a database for actual implentation
vet_list = ["Dr.Smith - Texas Livestock Care", "Dr.Burns - Farm Animal Hospital"] 
for vet in vet_list:
    st.write(f"- {vet}")

'''
#Disclaimer
st.write("\nNote: AVA's advice does not replace the advice of professonal veterinarians.")