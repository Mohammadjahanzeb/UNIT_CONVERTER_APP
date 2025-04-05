import streamlit as st

# Title
st.title("🔄 Unit Converter App")

# Conversion Types
conversion_types = ["Length", "Weight", "Temperature"]
conversion_choice = st.selectbox("Choose Conversion Type:", conversion_types)

# ==================== Length Conversion ====================
if conversion_choice == "Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    length_conversion = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }

    input_value = st.number_input("Enter Length Value:", min_value=0.0, format="%.2f", key="length_input")
    from_unit = st.selectbox("From Unit:", length_units, key="len_from")
    to_unit = st.selectbox("To Unit:", length_units, key="len_to")

    if st.button("Convert Length"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.2f} {to_unit}')

# ==================== Weight Conversion ====================
elif conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    weight_conversion = {
        "Kilograms": 1.0,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    input_value = st.number_input("Enter Weight Value:", min_value=0.0, format="%.2f", key="weight_input")
    from_unit = st.selectbox("From Unit:", weight_units, key="wt_from")
    to_unit = st.selectbox("To Unit:", weight_units, key="wt_to")

    if st.button("Convert Weight"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f'{input_value} {from_unit} = {result:.2f} {to_unit}')

# ==================== Temperature Conversion ====================
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter Temperature Value:", format="%.2f", key="temp_input")
    from_unit = st.selectbox("From Unit:", temperature_units, key="temp_from")
    to_unit = st.selectbox("To Unit:", temperature_units, key="temp_to")

    def convert_temperature(value, from_u, to_u):
        if from_u == to_u:
            return value
        if from_u == "Celsius":
            if to_u == "Fahrenheit":
                return (value * 9 / 5) + 32
            elif to_u == "Kelvin":
                return value + 273.15
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return (value - 32) * 5 / 9
            elif to_u == "Kelvin":
                return (value - 32) * 5 / 9 + 273.15
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return value - 273.15
            elif to_u == "Fahrenheit":
                return (value - 273.15) * 9 / 5 + 32

    if st.button("Convert Temperature"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value} {from_unit} = {result:.2f} {to_unit}')
