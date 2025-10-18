import streamlit as st
from descriptions import *
from heatmap import show_heatmap
from helpers import st_slider

# Streamlit page configuration
st.set_page_config(layout="wide")

st.title("🂡 🂭 Blackjack Monte Carlo Simulation")
mc_description()

n_simulations = st_slider("Number of simulations per cell",1,4000,500)
show_heatmap(n_simulations)