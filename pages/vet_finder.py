import streamlit as st

def show_vet_finder():
    st.title("Find a Veterinarian/Animal Specialist")
    st.write("Need help? Enter your zip code or city to get connected with a qualifed professional.")

    vet_location = st.text_input("Enter your location")
    if st.button("Submit"):
        #placeholder for now
        if vet_location:
            st.write(f"Searching for vets in **{vet_location}**...") 
        else:
            st.warning("Please enter the name of your city or zipcode before proceeding.")

    #Takes user back to the home screen
    if st.button("Main Menu"):
        st.session_state.page = "menu"
        st.rerun()