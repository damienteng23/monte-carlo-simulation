from .services import simulate_round
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random

# --- Streamlit UI ---
def show_heatmap(n_simulations=500):
    st.markdown("Simulating win rates for player hand totals vs dealer upcards.")

    player_totals = range(4, 22)
    dealer_upcards = [2,3,4,5,6,7,8,9,10,11]  # 11 = Ace

    heatmap_data = np.zeros((len(player_totals), len(dealer_upcards)))

    with st.spinner("Running simulations..."):
        for i, pt in enumerate(player_totals):
            for j, du in enumerate(dealer_upcards):
                heatmap_data[i, j] = simulate_round(pt, du, n=n_simulations)

    # --- Plot Heatmap ---
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".2f",
                xticklabels=dealer_upcards, yticklabels=player_totals,
                cmap="coolwarm", cbar_kws={'label': 'Win Rate'}, ax=ax)
    ax.set_xlabel("Dealer Upcard")
    ax.set_ylabel("Player Total")
    ax.set_title("Player Win Rate vs Dealer Upcard")

    st.pyplot(fig)