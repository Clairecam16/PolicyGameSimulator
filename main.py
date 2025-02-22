import streamlit as st
import numpy as np
import plotly.graph_objects as go
from game_logic import GameState, make_ai_decision
from visualizations import create_payoff_matrix_heatmap
from educational_content import display_educational_content
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Fiscal Policy Nash Equilibrium Game",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = GameState()

# Title and Introduction
st.title("🎯 Nash Equilibrium Fiscal Policy Game")

# Main game interface
col1, col2 = st.columns([2, 1])

with col1:
    # Display current scenario
    st.header("📊 Current Economic Scenario")
    scenario = st.session_state.game_state.current_scenario

    st.subheader(f"🌍 {scenario.name}")
    st.write(scenario.description)

    with st.expander("See Historical Context"):
        st.write(f"**Context:** {scenario.context}")
        st.write(f"**Historical Example:** {scenario.historical_example}")

    # Display payoff matrix visualization
    st.subheader("📈 Payoff Matrix for Current Scenario")
    fig = create_payoff_matrix_heatmap(scenario.payoff_modifiers)
    st.plotly_chart(fig)

    # Player's choice
    player_choice = st.radio(
        "📌 Choose your fiscal policy:",
        ["Austerity", "Stimulus"],
        help="Consider the current economic scenario carefully!"
    )

    # Create two columns for the buttons
    button_col1, button_col2 = st.columns(2)

    with button_col1:
        if st.button("Make Decision", key="decision_button", use_container_width=True):
            # AI makes its choice
            ai_choice = make_ai_decision(st.session_state.game_state)

            # Update game state
            payoff1, payoff2 = st.session_state.game_state.get_payoffs(player_choice, ai_choice)
            st.session_state.game_state.update_history(player_choice, ai_choice, payoff1, payoff2)

            # Display results
            st.write(f"💡 AI Policymaker chose: **{ai_choice}**")
            st.write(f"📈 Your Payoff: **{payoff1}** | 📉 AI's Payoff: **{payoff2}**")

            # Check for Nash Equilibrium
            if st.session_state.game_state.is_nash_equilibrium(player_choice, ai_choice):
                st.success("🎯 This is a Nash Equilibrium! Neither player would benefit from changing their strategy.")
            else:
                st.warning("⚠️ This is NOT a Nash Equilibrium. At least one player could benefit from changing their strategy.")

    with button_col2:
        # Next scenario button (outside the decision button conditional)
        if st.button("Next Scenario", key="next_scenario", use_container_width=True):
            st.session_state.game_state.next_scenario()
            st.rerun()

with col2:
    # Educational content in sidebar
    display_educational_content()

    # Game Statistics
    st.subheader("📊 Game Statistics")
    stats = st.session_state.game_state.get_statistics()

    st.metric("Games Played", stats['games_played'])
    st.metric("Nash Equilibria Reached", stats['nash_equilibria'])
    st.metric("Average Payoff", round(stats['avg_payoff'], 2))

    # Recent History
    st.subheader("🕒 Recent Moves")
    history_df = pd.DataFrame(st.session_state.game_state.history[-5:])
    if not history_df.empty:
        st.dataframe(history_df)

# Reset button
if st.button("Reset Game"):
    st.session_state.game_state = GameState()
    st.rerun()