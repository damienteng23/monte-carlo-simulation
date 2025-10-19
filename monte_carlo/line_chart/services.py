from histogram.services import simulate_hand
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulate_bankroll(num_hands, base_bet):
    bankroll = [0]
    total = 0

    for _ in range(num_hands):
        player_hand = simulate_hand('player')
        dealer_hand = simulate_hand('dealer')

        for p_total in player_hand:  # handles splits
            d_total = dealer_hand[0]  # dealer only has one hand

            # Check for blackjack
            if p_total == 21 and len(player_hand) == 1:
                total += base_bet * 1.5
            elif p_total > 21:
                total -= base_bet
            elif d_total > 21:
                total += base_bet
            elif p_total > d_total:
                total += base_bet
            elif p_total < d_total:
                total -= base_bet
            else:
                total += 0  # draw

            bankroll.append(total)

    return bankroll