import streamlit as st

def st_slider(label, min_val, max_val, default_val):
    return st.slider(label, min_value=min_val, max_value=max_val, value=default_val)