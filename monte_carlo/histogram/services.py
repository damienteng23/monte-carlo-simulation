import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Card actions
def draw_card():
    card = np.random.choice(['A'] + list(range(2, 11)) + ['J', 'Q', 'K'])
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11  # Start as 11, adjust later
    else:
        return int(card)

def adjust_for_ace(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Simulate one hand
def simulate_hand(strategy='player'):
    hand = [draw_card(), draw_card()]
    total = adjust_for_ace(hand)

    while total < 17:
        hand.append(draw_card())
        total = adjust_for_ace(hand)
    return total

# Run simulation
def simulate_totals(num_hands, strategy='player'):
    return [simulate_hand(strategy) for _ in range(num_hands)]