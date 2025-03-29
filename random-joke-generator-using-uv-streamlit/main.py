import streamlit as st
import requests

def get_random_joke():
    """fetch a random joke from the api"""
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        if response.status_code == 200:  #200 means api run successfully , 400 mean error
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again"
    
    except Exception as e:
        return "why did the programmer quit his job? \n because he didn't get arrays!" 
    

def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random job")

    if st.button("Generate a joke!"):
        joke = get_random_joke()
        st.success(joke)

    st.divider()

    

    st.markdown(
        """
                              
  
                <div style="text-align:center">
                    <p>joke from official joke API</p>
                    <p>Build with 💓 by <a href=""> SARFRAZ AZIZ</a> using Streamlit</p>
                </div>

        """,unsafe_allow_html=True) 

if __name__ == "__main__":
    main()