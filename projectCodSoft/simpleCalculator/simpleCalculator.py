import streamlit as st

# Function to perform the calculation based on selected operation
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

# Title and header
st.title("Basic Calculator")
st.header("Perform basic arithmetic operations")

# Input fields for numbers
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Dropdown menu for operation selection
operation = st.selectbox("Select operation:", ["+", "-", "*", "/"])

# Button to trigger calculation
if st.button("Calculate"):
    # Perform calculation and display result
    result = calculate(num1, num2, operation)
    st.write("Result:", result)
