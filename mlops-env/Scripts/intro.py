import streamlit as st

st.title("This is first stremalit app with lots of features")

import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Good JOB")



genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Jandhyala is the king of comedy.",
        "Rajamouli is the king of drama.",
        "Never stop learning.",
    ],
)


