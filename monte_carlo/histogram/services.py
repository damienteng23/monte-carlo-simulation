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
def simulate_hand(strategy):
    hand = [draw_card(), draw_card()]
    total = adjust_for_ace(hand)

    # Dealer hits until 17 or more, no splits or double downs
    if strategy == 'dealer':
        while total < 17:
            hand.append(draw_card())
            total = adjust_for_ace(hand)
        return [total]

    # Player strategy: split if pair and total < 17
    if hand[0] == hand[1] and total < 17:
        split_totals = []
        for card in hand:
            split_hand = [card, draw_card()]
            split_total = adjust_for_ace(split_hand)
            while split_total < 17:
                split_hand.append(draw_card())
                split_total = adjust_for_ace(split_hand)
            split_totals.append(split_total)
        return split_totals

    # Normal player strategy: hit below 17
    while total < 17:
        hand.append(draw_card())
        total = adjust_for_ace(hand)

    return [total]

# Run simulation
def simulate_totals(num_hands, strategy):
    results = []
    for _ in range(num_hands):
        results.extend(simulate_hand(strategy))
    return results