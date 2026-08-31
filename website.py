import colorama as cl
import streamlit as st
import random as rd
import time
import os

st.title("sheet-generato")
st.write("Converting raw data into a clean sheet\n\n")

data = st.chat_input("what is your name\n")
