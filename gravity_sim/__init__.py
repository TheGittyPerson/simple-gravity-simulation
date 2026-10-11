__name__ = "simple-gravity-simulator"
__version__ = "0.1.0"

from .simulation import Simulation
from .body import Body
from .engine import Engine
from .event_handler import EventHandler
from .settings_parser import SettingsParser

__all__ = ["Simulation", "Body", "Engine", "EventHandler", "SettingsParser"]
