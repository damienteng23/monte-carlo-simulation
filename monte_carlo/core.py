import streamlit as st
from descriptions import *
from circle_in_square import mc_pi
from heatmap import show_heatmap
from helpers import st_slider

# Streamlit page configuration
st.set_page_config(layout="wide")
st.sidebar.title("Find Me")

st.title("🂡 🂭 Monte Carlo Simulation")

# region Descriptions
col1, col2 = st.columns(2)

with col1:
    st.subheader("So... what is Monte Carlo? 🙋🏻‍♂️")
    description_what_is_monte_carlo()

with col2:
    st.subheader("Fun fact 😄")
    description_fun_fact()
# endregion

# region Circle in Square 
col1, col2 = st.columns(2)

with col2:
    pi_simulations = st_slider("Number of Random Points",1,100000,100)
    error_percent = mc_pi(pi_simulations)

with col1:
    st.subheader("Finding Patterns? 🤔")
    description_finding_patterns()
    st.metric(label="π Estimation Error", value=f"{error_percent:.8f}%", delta=f"{-error_percent:.8f}%")
# endregion

# region What if
st.subheader("What if....? 💵🤑")
description_what_if()
# endregion

# region Blackjack description
st.subheader("Alrights, enough theory! Let's simulate some Blackjack! 🃏")
description_blackjack_assumptions()
# endregion

# region Heatmap
col1, col2 = st.columns(2)

with col1:
    n_simulations = st_slider("Number of simulations per cell",1,4000,500)
    show_heatmap(n_simulations)

with col2:
    st.subheader("Heatmap Simulation Results 📊")
    description_heatmap_simulation_results()

#endregion