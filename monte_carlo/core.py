import streamlit as st
from heatmap import show_heatmap
from helpers import st_slider

st.set_page_config(layout="wide")

n_simulations = st_slider("Number of simulations per cell",1,4000,500)
show_heatmap(n_simulations)