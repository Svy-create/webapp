import streamlit as st 


print("Hello")

with st.form ('Form2') : 

    # On demande à l'utilisateur son nom 
    user_name =  st.text_input('Tape your name: ')

    # On demande à l'utilisateur son prénom
    user_first_name = st.text_input('Tape your Firstname')

    user_age = st.select_slider("Please select your age",
                                 options= range (18, 99))

    user_graduation = st.selectbox(
    "Select your graduation?",
    ("Sans diplôme", "BAC", "BAC+3", "BAC+5"))

    # Bouton "Envoyer"
    if st.form_submit_button('Send'): 
        st.write('Form Submitted')
    


# Nom


# Prénom 

# Age 

# Niveau d'étude 

