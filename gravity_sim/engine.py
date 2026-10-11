"""Contains the physics engine class that decides what happens
next and updates Body states.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gravity_sim import Simulation


class Engine:
    """Controls interactions between Bodies and updates their states."""

    def __init__(self, sim: Simulation):
        self.sim = sim
