import streamlit as st
from descriptions import *
from circle_in_square import mc_pi
from heatmap import show_heatmap
from helpers import st_slider

# Streamlit page configuration
st.set_page_config(layout="wide")
st.sidebar.title("Find Me")

pi_simulations = st_slider("Number of Random Points",1,100000,100)
mc_pi(pi_simulations)

st.title("🂡 🂭 Blackjack Monte Carlo Simulation")
st.subheader("So, what is Monte Carlo? ")
mc_description()

n_simulations = st_slider("Number of simulations per cell",1,4000,500)
show_heatmap(n_simulations)