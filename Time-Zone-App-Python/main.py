import streamlit as st # aliasing streamlit as st
from datetime import datetime # importing class datetime from module datetime
from zoneinfo import ZoneInfo  

st.set_page_config(page_title="Time Zone App", layout="wide") # setting the page title and layout


dark_mode = """
    <style>
    .stMainBlockContainer {
        # background-image: url("D:\generative ai course\quarter 3 python\Ramzan-Coding-Night-Python-Project\Time-Zone-App-Python\images");
        background-color: grey;
        
        }


    .stVerticalBlock  {
        background-color: rgba(0, 0, 0, 0.85); /* Semi-transparent black */
        padding: 20px;
        border-radius: 10px;
        color: white;
        max-width: 800px;
        margin: auto;

    }
    </style>
"""
st.markdown(dark_mode, unsafe_allow_html=True)


#list of available timezones
TIME_ZONE = [                       #CAPTITAL LETTERS ARE CONSTANTS VARIABLES   
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]


        

st.title("Time Zone App")

selected_timezone = st.multiselect("Select TimeZones", TIME_ZONE, default=["UTC", "Asia/Karachi"])

st.subheader("Selected TimeZones")

for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d  %I:%M:%S %p") 
        #strftime is a method that returns a string representing the date, controlled by an explicit format string.
                                                                                    # %p is used for AM/PM and %i is used for 12 hour clock

    st.write(f" **{tz}**: {current_time}")    #** is used for bold text 




st.subheader("Convert Time Between TimeZones")

current_time = st.time_input("Current Time", value=datetime.now().time()) #time_input is used to take time input from user

from_tz = st.selectbox("From TimeZone", TIME_ZONE, index=0) #selectbox is used to take input from user and index is used to set the default value

to_tz = st.selectbox("To TimeZone", TIME_ZONE, index=1)


if st.button("Convert Time"): #button is used to create button
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz)) #combine is used to combine date and time , tzinfo=ZoneInfo() is used to set the timezone
    
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d  %I:%M:%S %p")    #astimezone is used to convert time to the given timezone
    
    st.success(f"Converted Time in {to_tz}: {converted_time}")   






