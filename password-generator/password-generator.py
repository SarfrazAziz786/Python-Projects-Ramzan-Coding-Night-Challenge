import streamlit as st  # type: ignore
import random 
import string # string module use for specific characters uppercase, lowercase, digits, special characters

def generate_password(Length, use_digits, use_special):
    characters = string.ascii_letters # use for uppercase and lowercase letters
    if use_digits:
        characters += string.digits # use for digits (0-9)
    if use_special:
        characters += string.punctuation # use for special characters (@, !, #, $, %, ^, &, *)

    return ''.join(random.choice(characters) for _ in range(Length)) # join the characters together,' _ ' use for the length of the password

st.title("Password Generator")

length = st.slider("Select the length of the password", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: {password}")

st.write("--------------------------------")




