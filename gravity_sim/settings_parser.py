"""Contains the `Settings` class to control user-configurable settings."""

from configparser import ConfigParser
from pathlib import Path
from platformdirs import user_config_dir

from . import __name__, __version__


class SettingsParser:
    """Manage and parse user-configurable settings file."""
    CONFIG_NAME = "settings.ini"

    def __init__(self):
        # self.config_dir: str = user_config_dir(__name__, version=__version__)
        # Store in project root for now so that we can easily change settings.
        # Later, we use the one above instead.
        self.config_dir: Path = Path(__file__).parent.parent
        self.config_file: Path = Path(self.config_dir) / self.CONFIG_NAME

        self.config: ConfigParser = ConfigParser()
