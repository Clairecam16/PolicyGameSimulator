import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import random

@dataclass
class EconomicScenario:
    name: str
    description: str
    context: str
    historical_example: str
    payoff_modifiers: Dict[Tuple[str, str], Tuple[int, int]]

# Define various economic scenarios
ECONOMIC_SCENARIOS = [
    EconomicScenario(
        name="Global Financial Crisis",
        description="A severe economic downturn has caused widespread unemployment and market instability.",
        context="Banks are failing and credit markets are frozen. Quick action is needed.",
        historical_example="Similar to the 2008 Financial Crisis where many countries had to decide between austerity and stimulus packages.",
        payoff_modifiers={
            ("Austerity", "Austerity"): (2, 2),  # Both choosing austerity is worse during crisis
            ("Austerity", "Stimulus"): (3, 5),   # Free-riding on other's stimulus
            ("Stimulus", "Austerity"): (5, 3),   # Free-riding on other's stimulus
            ("Stimulus", "Stimulus"): (4, 4),    # Coordinated stimulus is better during crisis
        }
    ),
    EconomicScenario(
        name="Post-War Recovery",
        description="The economy is rebuilding after a major conflict, with high government debt but growth opportunities.",
        context="Infrastructure needs rebuilding, but government coffers are strained.",
        historical_example="Similar to the Marshall Plan after World War II, where countries had to balance recovery spending with fiscal restraint.",
        payoff_modifiers={
            ("Austerity", "Austerity"): (3, 3),
            ("Austerity", "Stimulus"): (2, 4),
            ("Stimulus", "Austerity"): (4, 2),
            ("Stimulus", "Stimulus"): (5, 5),
        }
    ),
    EconomicScenario(
        name="Inflationary Pressure",
        description="Rapidly rising prices are eroding purchasing power and economic stability.",
        context="Central banks are raising interest rates, and government spending is under scrutiny.",
        historical_example="Similar to the 1970s stagflation period, where governments had to balance growth with inflation control.",
        payoff_modifiers={
            ("Austerity", "Austerity"): (4, 4),  # Austerity more valuable during inflation
            ("Austerity", "Stimulus"): (3, 2),
            ("Stimulus", "Austerity"): (2, 3),
            ("Stimulus", "Stimulus"): (1, 1),    # Double stimulus worse during inflation
        }
    ),
]

@dataclass
class GameState:
    current_scenario: EconomicScenario = field(default_factory=lambda: random.choice(ECONOMIC_SCENARIOS))
    history: List[Dict] = field(default_factory=list)

    def get_payoffs(self, player1_choice: str, player2_choice: str) -> Tuple[int, int]:
        return self.current_scenario.payoff_modifiers[(player1_choice, player2_choice)]

    def is_nash_equilibrium(self, player1_choice: str, player2_choice: str) -> bool:
        current_payoff = self.current_scenario.payoff_modifiers[(player1_choice, player2_choice)]

        # Check if Player 1 can improve by switching
        other_choice = "Stimulus" if player1_choice == "Austerity" else "Austerity"
        if self.current_scenario.payoff_modifiers[(other_choice, player2_choice)][0] > current_payoff[0]:
            return False

        # Check if Player 2 can improve by switching
        other_choice = "Stimulus" if player2_choice == "Austerity" else "Austerity"
        if self.current_scenario.payoff_modifiers[(player1_choice, other_choice)][1] > current_payoff[1]:
            return False

        return True

    def update_history(self, player_choice: str, ai_choice: str, player_payoff: int, ai_payoff: int):
        self.history.append({
            'Scenario': self.current_scenario.name,
            'Player Choice': player_choice,
            'AI Choice': ai_choice,
            'Player Payoff': player_payoff,
            'AI Payoff': ai_payoff,
            'Nash Equilibrium': self.is_nash_equilibrium(player_choice, ai_choice)
        })

    def next_scenario(self):
        self.current_scenario = random.choice(ECONOMIC_SCENARIOS)

    def get_statistics(self) -> Dict:
        if not self.history:
            return {
                'games_played': 0,
                'nash_equilibria': 0,
                'avg_payoff': 0.0
            }

        return {
            'games_played': len(self.history),
            'nash_equilibria': sum(1 for game in self.history if game['Nash Equilibrium']),
            'avg_payoff': sum(game['Player Payoff'] for game in self.history) / len(self.history)
        }

def make_ai_decision(game_state: GameState) -> str:
    """
    AI strategy that adapts to the current economic scenario
    """
    scenario = game_state.current_scenario

    # Base strategy on scenario type
    if scenario.name == "Global Financial Crisis":
        return "Stimulus" if random.random() < 0.7 else "Austerity"  # Favor stimulus during crisis
    elif scenario.name == "Inflationary Pressure":
        return "Austerity" if random.random() < 0.7 else "Stimulus"  # Favor austerity during inflation
    else:
        # Mixed strategy for other scenarios
        return np.random.choice(["Austerity", "Stimulus"], p=[0.5, 0.5])