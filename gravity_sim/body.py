"""Contains the `Body` class."""

from typing import TYPE_CHECKING

from pygame.sprite import Sprite

if TYPE_CHECKING:
    from .simulation import Simulation


class Body(Sprite):
    """Represents an individual body on screen."""
    def __init__(self, sim: Simulation):
        super().__init__()
        self.sim = sim
        ...
