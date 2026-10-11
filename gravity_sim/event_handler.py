"""Contains the `EventHandler` class that responds to user events."""
from gravity_sim import Simulation


class EventHandler:
    """Catches and responds to user events."""

    def __init__(self, sim: Simulation):
        self.sim = sim
