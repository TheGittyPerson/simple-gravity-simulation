"""This is the main module to instantiate a run a simulation."""

import pygame


class Simulation:
    """Central class to run the simulation."""

    def __init__(self):
        pygame.init()

    def run(self) -> None:
        ...
