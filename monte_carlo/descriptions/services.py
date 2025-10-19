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
            - **Double Down**: Double bet, take one card, then stand.
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
        "The heatmap visualizes our win rates, darker reds indicate higher "
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
        Let's play with a simple strategy to maximize our win rate against the house! 
        - Assume that after observing the heatmap, players will always stand on 17 or higher, else 
        player will hit
        - Players will also always draw whenver he/she is below 17
    """)
