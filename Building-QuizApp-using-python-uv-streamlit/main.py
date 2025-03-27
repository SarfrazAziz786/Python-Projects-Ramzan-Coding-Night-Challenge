import streamlit as st #web interface
import random
import time #for delay in seconds

st.markdown("""
    <style>
        /* Apply styles to the entire Streamlit app */
        .stApp {
            font-family: 'Arial', sans-serif;
            background-color: gold;
            color: black;
        }
            
        .stButton {
            color: white;
            }
    
    .stRadio label {
        color: black;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)


st.title("⁜Quiz Application⁜")

questions = [
    {
        "question": "What is the output of the compilation step in the Python execution engine?",
        "options": ["(a) Native machine code ", "(b) Python source code", "(c) Bytecode (.pyc files)", "(d)- Intermediate representation (IR)"],
        "answer":   "(c) Bytecode (.pyc files)"},
    {
        "question": "Which of the following is a mapping data type in Python?",
        "options": ["(a)Dictionary ", "(b)Virtual Machine (PVM)", "(c)- Just-In-Time (JIT) compiler", "(d) Static type checker"], 
        "answer":   "(a)Dictionary "},
    { 
        "question": "What happens if the indentation in a Python program is incorrect?",
        "options": ["(a)  The program will run slower", "(b) The program will produce incorrect results", "(c) The program will raise a syntax error", "(d)  The program will ignore the incorrect indentation"], 
        "answer":   "(c) The program will raise a syntax error" },

    
]

#streamlit session state same as state nextjs
#initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions) 

#Get the current question from the session state
question = st.session_state.current_question

#Display the question
st.subheader(question["question"])

#Create a radio button for the option 
selected_option = st.radio("Choose your answer", question["options"], key="answer") #select box for radio buttons

#submit button  to the answer
if st.button("Submit Answer"):
    
    if selected_option == question["answer"]:
        st.success("Correct!")
        st.balloons()
    else:
        st.error("❌Incorrect! the correct answer is " + question["answer"])
    
    #after 3 seconds, load the next question
    time.sleep(1)
    
    #select a new random question
    st.session_state.current_question = random.choice(questions)

    #rerun the app to the new question
    st.rerun()











