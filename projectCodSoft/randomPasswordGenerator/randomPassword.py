import streamlit as st
import random

# Character sets for password generation
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
digits = "0123456789"
symbols = "!@#$%^&*()"
all_chars = lowercase + uppercase + digits + symbols

def generate_password(length, include_uppercase, include_digits, include_symbols):
  """
  Generates a random password based on specified criteria.

  Args:
      length (int): Desired length of the password.
      include_uppercase (bool): Whether to include uppercase letters.
      include_digits (bool): Whether to include digits.
      include_symbols (bool): Whether to include symbols.

  Returns:
      str: The generated random password.
  """
  password_chars = ""
  if include_uppercase:
    password_chars += uppercase
  if include_digits:
    password_chars += digits
  if include_symbols:
    password_chars += symbols
  password_chars += lowercase  # Always include lowercase

  # Shuffle the character pool for better randomness
  random.shuffle(list(password_chars))

  # Generate password by selecting characters from the shuffled pool
  password = ''.join(random.choices(password_chars, k=length))
  return password

# Title and input fields
st.title("Random Password Generator")

password_length = st.number_input("Password Length (8-32 characters)", min_value=8, max_value=32, value=16)
include_uppercase = st.checkbox("Include Uppercase Letters")
include_digits = st.checkbox("Include Digits")
include_symbols = st.checkbox("Include Symbols")

# Generate button and password display
if st.button("Generate Password"):
  generated_password = generate_password(password_length, include_uppercase, include_digits, include_symbols)
  st.write("Your Generated Password:")
  st.code(generated_password)  # Display password in code block for better visibility

# Info message
st.info("**Security Tip:** Use a strong password with a mix of uppercase and lowercase letters, digits, and symbols. Don't reuse passwords across different websites or services.")
