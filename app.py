""" Streamlit app to play a number guessing game. """
import random
import streamlit as st



st.title("Guess the Number Game")

st.write("I'm thinking of a number between 1 and 100.")

with st.form("number-guessing-form"):
    if 'guess' not in st.session_state:
        st.session_state.guess = random.randint(1, 100)

    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0

    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.form_submit_button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.guess:
            st.write("Too low! Try again.")
        elif guess > st.session_state.guess:
            st.write("Too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.balloons()