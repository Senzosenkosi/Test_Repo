import pandas as ps 
import streamlit as st
print("welocome to my page")
import time

st.write("my first app is write here")
st.balloons()
st.set_page_config(
    page_title="Stock Info",
    page_icon="🏛️",
)
st.markdown("## Question 1.")
countdown = st.empty()
for i in range(30, 0, -1):
    countdown.markdown(f"## Countdown: {i} seconds")
    time.sleep(1)
countdown.markdown("## Time's up!")