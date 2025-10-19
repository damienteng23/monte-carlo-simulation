import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from .services import simulate_totals

def show_histogram(num_hands):
    num_hands = st.slider("Number of Simulated Hands", 1, num_hands)

    player_totals = simulate_totals(num_hands)
    dealer_totals = simulate_totals(num_hands)

    bins = list(range(2, 23))
    player_counts = [player_totals.count(b) for b in bins]
    dealer_counts = [dealer_totals.count(b) for b in bins]

    x = np.arange(len(bins))
    width = 0.4

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - width/2, player_counts, width, label='Player', color='blue')
    ax.bar(x + width/2, dealer_counts, width, label='Dealer', color='orange')

    ax.set_xticks(x)
    ax.set_xticklabels(bins)
    ax.set_xlabel("Final Hand Total")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Final Hand Sum for {num_hands} Simulated Hands")
    ax.legend()

    st.pyplot(fig)