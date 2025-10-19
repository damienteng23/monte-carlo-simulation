import streamlit as st

def description_what_is_monte_carlo():
    st.write(
        "Also known as the Monte Carlo Method or a multiple probability simulation, "
        "It is a mathematical technique used to estimate the possible outcomes of an "
        "uncertain event "
    )

def description_fun_fact():
    st.write(
        "The name 'Monte Carlo' was inspired by the Monte Carlo Casino in Monaco, "
        "reflecting the method's reliance on randomness and chance, similar to gambling games!"
    )

def description_why_bother():
    st.write(
        "The Monte Carlo method encompasses a class of statistical techniques that leverage "
        "random sampling to analyze and solve real-world problems. Due to its reliance on randomness, "
        "it is inherently stochastic and exhibits well-defined statistical characteristics. "
    )

def description_finding_patterns():
    st.write(
        "Using Monte Carlo simulation to estimate the value of π beautifully illustrates how "
        "random sampling can approximate deterministic constants through probability and geometry. "
    )
    with st.expander("See why this works"):
            st.write(
                "As the number of random points increases, the estimate of π becomes more accurate. "
                "This convergence towards the true value of π demonstrates the power of statistical methods "
                "in approximating mathematical constants!"
            )

def description_what_if():
    st.write(
        "Hmm... what if we could use Monte Carlo simulations to analyze and optimize strategies in Blackjack? "
        "By simulating numerous hands and outcomes, we can gain insights into the effectiveness of different "
        "player strategies and dealer behaviors in the game!"
    )

def description_blackjack_assumptions():
    col1, col2 = st.columns([1,2])

    with col1:
        st.write("""
            **🧩 Play Order**
            - Player receives 2 cards face up.
            - Dealer receives one upcard and one hole card.

            **🎯 Player Actions**
            - **Hit**: Take another card.
            - **Stand**: Keep current hand.
            - **Split**: If two cards are same value, split into two hands.
        """)

    with col2:
        st.write("""
            **📜 Rules**
            - Dealer must stand at a minimum of 17.
            - Players have no minimum hand value.
            - Picture cards (J, Q, K) are worth 10.
            - Cards 2–10 retain face value.
            - Aces are worth 1 or 11, whichever benefits the hand without busting.

            **💰 Payouts**
            - Blackjack pays **3 to 2**
            - All other wins (including splits) pay **1 to 1**
        """)

def description_simulation_details():
    st.write(
        "In this simulation, we will run multiple iterations of Blackjack hands, "
        "varying player strategies and dealer behaviors to analyze outcomes. "
        "By aggregating results across numerous simulations, we can identify optimal strategies "
        "and understand the statistical dynamics of the game!"
    )

def description_heatmap_simulation_results():
    st.write(
        "We can visualize strategic strength of hand combinations! Darker reds indicate higher "
        "win rates, allowing us to quickly identify optimal plays! "
    )
    with st.expander("What does this tell us?"):
        st.write("""
            - Player totals of 19–21 consistently yield the highest win rates across all dealer upcards
            - Dealer upcards of 2–6 (often called “bust cards”) correlate with higher player win rates
            - Dealer upcards of 10 or 11 (strong cards) significantly reduce player win rates
            - Low Player Totals Are Risky
            - Convergence(stabilization and improvements in win rate) begins Around 17
        """)
    with st.expander("What should we do?"):
        st.write("""
            - Stand on 17+ when facing dealer 2–6: high win probability
            - Be cautious with totals ≤16, especially against dealer 7–11
            - Use splits and doubles tactically to escape low-win-rate zones
            - Dealer strength is pivotal—adjust your strategy based on their upcard, not just your total
        """)

def description_win_rate():
    st.write("""
        We will now track the sum of the final hand of the players/dealers after each game, and plot a histogram to see the distribution. 
        Let's play with a simple strategy to maximize our win rate against the house! 
        - Assume that after observing the heatmap, players will always stand on 17 or higher, else 
        player will hit
        - Assume that after observing the heatmap, if players draw a same value pair below 17, he/she will always split
    """)

def description_win_rate_2():
    st.write(
        "Increase the number of plays to get a more accurate representation of your win rate against the house, " 
        "what do you observe as you increase the number of plays? "
    )
    with st.expander("This seems odd, the odds doesnt seem to be that much better than the dealers..."):
        st.write(
            "As you increase the number of plays, the histogram should start to resemble a normal distribution due to the Central Limit Theorem. "
            "This means that the results will cluster around the mean win rate, providing a clearer picture of your performance against the house. "
            "This histogram also assumes that dealer will not implement any strategies, and will always hit below 17 and stand on 17 or higher."
        )
    with st.expander("Central Limit Theorem?"):
        st.write(
            "When you take a large number of random samples from any population (regardless of its original distribution), "
            "the distribution of the sample means will tend to be normal (bell-shaped). "
        )

def description_bankroll_result():
    st.write(
        "The bankroll trajectory chart illustrates how your cumulative profit or loss evolves over time as you play multiple hands of Blackjack. "
        "By simulating a series of hands, we can visualize the fluctuations in your bankroll based on wins, losses, and draws against the dealer."
    )
    with st.expander("How should I interpret this chart? 🤔"):
        st.write("""
            - **Upward Trends**: Indicate periods of consistent wins, suggesting effective strategies.
            - **Downward Trends**: Reflect losing streaks, highlighting potential weaknesses in strategy.
            - **Volatility**: Frequent fluctuations may suggest high-risk strategies; steadier lines indicate more conservative play.
            - **Break-even Points**: Points where the bankroll crosses the initial value can indicate shifts in luck or strategy effectiveness.
        """)
    with st.expander("What am I looking at? 😟"):
        st.write("""
            Even with basic strategy, the casino has a built-in edge — typically around 0.5% to 1%. Over thousands of hands, this edge compounds, slowly draining your bankroll.
            Here’s how the edge is baked into the rules:
        """)
        st.table({
            "Rule or Mechanic": [
                "Dealer acts last",
                "Dealer wins ties (in some games)",
                "No player-to-player interaction",
                "Blackjack pays 6:5 instead of 3:2",
                "Dealer hits on soft 17",
                "No double after split",
                "No resplit aces",
                "Limited splits",
                "No late surrender",
                "Continuous shuffle",
                "Eight-deck shoe"
            ],
            "How It Favors the House": [
                "Players bust before dealer plays — automatic loss",
                "Pushes are rare; house may win ties depending on rules",
                "You can’t team up or share info — house plays solo",
                "Lower payout increases house edge significantly",
                "Increases dealer win rate on borderline hands",
                "Reduces player flexibility and win potential",
                "Limits recovery options after splitting aces",
                "Restricts strategic hand separation",
                "Removes a valuable escape option for bad hands",
                "Prevents card counting and deck tracking",
                "Dilutes card counting and increases variance"
            ]
        })
