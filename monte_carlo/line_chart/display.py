from .services import simulate_bankroll
from descriptions.services import description_bankroll_result
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Streamlit UI
def show_bankroll_chart(num_hands, bet_size):
    st.title("📈 Bankroll Trajectory")
    st.subheader("Let's make it rain 💰!")
    description_bankroll_result()

    num_hands = st.slider("Number of Simulated Hands", 1, num_hands, 1)

    bankroll = simulate_bankroll(num_hands, bet_size)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(bankroll, color='green')
    ax.set_title("Cumulative Bankroll Over Time")
    ax.set_xlabel("Hand Number")
    ax.set_ylabel("Profit/Loss ($)")
    ax.axhline(0, color='gray', linestyle='--')
    st.pyplot(fig)