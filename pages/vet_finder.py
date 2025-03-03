import streamlit as st

st.title("Find a Veterinarian/Animal Specialist")
st.write("Need help? Enter your zip code or city to get connected with a qualifed professional.")

vet_location = st.text_input("Enter your location")
if st.button("Submit"):
    if vet_location:
        st.write(f"Searching for vets in **{vet_location}**...") #placeholder for now
    else:
        st.warning("Please enter the name of your city or zipcode before proceeding.")