import streamlit as st
from ui_components import render_sidebar, render_home, render_education, render_playground, render_quiz

# Page Configuration
st.set_page_config(page_title="FraudGuard AI", layout="wide", page_icon="🛡️")

def main():
    selection = render_sidebar()

    if selection == "Home":
        render_home()
    elif selection == "How it Works":
        render_education()
    elif selection == "Live Predictor":
        render_playground()
    elif selection == "Quiz & Trivia":
        render_quiz()

if __name__ == "__main__":
    main()
