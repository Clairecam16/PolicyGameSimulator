import plotly.graph_objects as go
import numpy as np
from typing import Dict, Tuple

def create_payoff_matrix_heatmap(payoff_matrix: Dict[Tuple[str, str], Tuple[int, int]]):
    """
    Creates a heatmap visualization of the payoff matrix for the current scenario
    """
    # Create matrices for player 1 and 2 payoffs
    player1_payoffs = np.array([
        [payoff_matrix[("Austerity", "Austerity")][0], payoff_matrix[("Austerity", "Stimulus")][0]],
        [payoff_matrix[("Stimulus", "Austerity")][0], payoff_matrix[("Stimulus", "Stimulus")][0]]
    ])

    player2_payoffs = np.array([
        [payoff_matrix[("Austerity", "Austerity")][1], payoff_matrix[("Austerity", "Stimulus")][1]],
        [payoff_matrix[("Stimulus", "Austerity")][1], payoff_matrix[("Stimulus", "Stimulus")][1]]
    ])

    # Create the heatmap
    fig = go.Figure(data=[
        go.Heatmap(
            z=player1_payoffs,
            x=['Austerity', 'Stimulus'],
            y=['Austerity', 'Stimulus'],
            text=[[f"({player1_payoffs[i][j]}, {player2_payoffs[i][j]})" 
                  for j in range(2)] for i in range(2)],
            texttemplate="%{text}",
            textfont={"size": 20},
            showscale=False,
            colorscale='RdYlBu'
        )
    ])

    fig.update_layout(
        title="Payoff Matrix (Player, AI)",
        xaxis_title="AI's Choice",
        yaxis_title="Player's Choice",
        width=500,
        height=500,
        font=dict(size=14)
    )

    return fig