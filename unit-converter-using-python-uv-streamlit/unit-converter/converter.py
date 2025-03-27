import streamlit as st

def convert_units(value, unit_from, unit_to):
    
    conversions= {
        "meter-kilometer": 0.001,  # 1 meter = 0.001 kilometer
        "kilometer-meter": 1000,    # 1 kilometer = 1000 meters
        "gram-kilogram": 0.001,     # 1 gram = 0.001 kilogram
        "kilogram-gram": 1000,      # 1 kilogram = 1000 grams
        }
    
    key = f"{unit_from}-{unit_to}"  #generate unique key for the conversion based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
st.title("Unit Converter")
value = st.number_input("Enter the value to convert", min_value=1.0 step=1.0)   # min value streamlit function to set the bydefault value to 1.0 and step function to set the increment value to 1.0

unit_from = st.selectbox("From", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("To", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")

    


