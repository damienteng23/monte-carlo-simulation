import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random


# Card values
def draw_card():
    card = random.randint(1, 13)
    if card >= 10:  # 10, J, Q, K
        return 10
    elif card == 1:  # Ace
        return 11
    else:
        return card

def hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def simulate_round(player_total, dealer_upcard, n=10000):
    wins, losses, pushes = 0, 0, 0
    for _ in range(n):
        # Dealer play
        dealer_hand = [dealer_upcard, draw_card()]
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(draw_card())
        dealer_val = hand_value(dealer_hand)

        # Compare outcomes
        if player_total > 21:
            losses += 1
        elif dealer_val > 21 or player_total > dealer_val:
            wins += 1
        elif player_total == dealer_val:
            pushes += 1
        else:
            losses += 1

    return wins / n  # win rate

# --- Streamlit UI ---
st.title("🎲 Blackjack Monte Carlo Simulation")
st.markdown("Simulating win rates for player hand totals vs dealer upcards.")

n_simulations = st.slider("Number of simulations per cell", min_value=1, max_value=1000, value=500)

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
