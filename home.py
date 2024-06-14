import streamlit as st 

#Titre
st.title("Hello world")

# Sous-Titre
st.subheader('This is a subheader')

#Texte 
st.write("This is a text")

# Champs de saisie 
user_input = st.text_input('Tape your text')

st.write (user_input)

st.image ('https://lh3.googleusercontent.com/proxy/w621npgqRBaCpQAv0oT8a9VoNONnSKTy8bT08T3ZrM3iLGOlx-hdswKlD2YQjYZ6V9zvEqUHgA2hCL40Qj4WIAnRmIl4BD1yRkJwMnbIYg')


# Créer un formulaire
with st.form ('Form1') : 

    # On demande à l'utilisateur son nom 
    user_name =  st.text_input('Tape your name: ')

    # Bouton "Envoyer"
    if st.form_submit_button("Send"): 
        # On affiche le nom de l'utilisateur
        st.write(user_name)



# Exercice 1 

