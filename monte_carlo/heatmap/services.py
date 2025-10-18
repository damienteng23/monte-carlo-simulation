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