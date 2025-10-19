import streamlit as st
from descriptions import *
from histogram import *
from circle_in_square import mc_pi
from heatmap import show_heatmap

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
    error_percent = mc_pi(100000)

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
    show_heatmap(4000)

with col2:
    st.subheader("Heatmap Simulation Results 📊")
    description_heatmap_simulation_results()

#endregion

# region Histogram
st.subheader("Okay... but how can I tell what is my actual win rate against the house? 📈")
st.title("Blackjack Final Hand Totals 🙏")
description_win_rate()

col1, col2 = st.columns(2)

with col1:
    st.write("test")

with col2:
    show_histogram(40000)

# endregion