import streamlit as st
import random # for random number generation
import time    # for time operations
import requests # for making HTTP requests

st.title("Money Making Machine") 

def generate_money():
    return random.randint(1, 1000) # generate a random integer between 1 and 1000 

st.subheader("Instant Cash Generator")   #subheader use to create a subheading

if st.button("Generate Money"): # button to generate money
    st.write("Counting your money...") # display message
    time.sleep(2) # wait for 2 seconds delay
    amount = generate_money() 
    st.success(f"Congratulations! You have generated {amount} $") # display success message



def fetch_side_hustle():    
    try:
        response = requests.get("http://127.0.0.1:8000/side-hustles") # .get use for get data from internet
        if response.status_code == 200: # status code received from the server
            hustles = response.json()
            return hustles["side_hustle"] # now showing the side hustle. no distionary format
        else:
            return ("Freelancing")
    except:
        return ("Something went wrong")
    
st.subheader("Side Hustle Ideas") #subheader use to create a subheading
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea) 


def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money-quotes") # .get use for get data from internet
        if response.status_code == 200: # status code received from the server
            quotes = response.json()
            return quotes["money_quote"] # now showing the quote. no distionary format
        else:
            return ("Money is the root of all evil")    

    except:
        return ("Something went wrong")
    
st.subheader("Money Making Motivation") #subheader use to create a subheading
if st.button("Generate Quote"):
    quote = fetch_money_quotes()
    st.success(quote)