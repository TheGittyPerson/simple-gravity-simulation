"""Contains the `Settings` class to control user-configurable settings."""
import copy
import json
from pathlib import Path
from typing import Any

# from platformdirs import user_config_dir

# from . import __name__, __version__


class SettingsParser:
    """Manage and parse user-configurable settings file."""
    CONFIG_NAME: str = "settings.json"
    DEFAULTS: dict[str, dict[str, Any]] = {
        "window": {
            "width": 800,
            "height": 600,
            "bg_color": [0, 0, 0],
        },
        "bodies": {
            "color": [255, 255, 255],
        }
    }

    def __init__(self):
        """Initialize attribute."""
        # self.file_dir: str = user_config_dir(__name__, version=__version__)
        # Store in project root for now so that we can easily change settings.
        # Later, we use the one above instead.
        self.file_dir: Path = Path(__file__).parent.parent
        self.file_path: Path = Path(self.file_dir) / self.CONFIG_NAME

        self.settings: dict[str, dict[str, Any]] = {}

        if not self.file_path.is_file():
            self._use_defaults()
            self._save_to_file()
        else:
            self._load_from_file()

    def get(self, section: str, option: str) -> Any:
        """Get the requested setting. Uses default if not found."""
        if not self._is_section(section):
            raise KeyError(f"Invalid section '{section}'")
        if not self._is_option(section, option):
            raise KeyError(f"Invalid option '{option}'")

        try:
            return self.settings[section][option]
        except KeyError:
            print(f"Setting '{section}', '{option}' not found. Using default")
            return self.DEFAULTS[section][option]

    def _is_section(self, section: str) -> bool:
        """Check if the section exists in the default settings dict."""
        return section in self.settings

    def _is_option(self, section: str, option: str) -> bool:
        """Check if the option exists in the default settings dict."""
        if not self._is_section(section):
            return False
        return option in self.DEFAULTS[section]

    def _get_default(self, section: str,
                     option: str) -> Any:
        """Get the default value for the specified setting option.

        Use when settings is not found or is invalid in the user's
        JSON file.
        """
        if not self._is_option(section, option):
            raise KeyError(
                f"Default setting '{section}', '{option}' not defined"
            )
        return self.DEFAULTS[section][option]

    def _use_defaults(self) -> None:
        """Fill `settings` dict with default settings."""
        self.settings = copy.deepcopy(self.DEFAULTS)

    def _load_from_file(self) -> None:
        """Get settings from the JSON file and store it in `settings` dict."""
        if not self.file_path.is_file():
            raise FileNotFoundError("Settings file not found.")
        try:
            with open(self.file_path, "r") as f:
                self.settings = json.load(f)
        except (json.JSONDecodeError, EOFError):
            print("Could not decode JSON file. Using default settings.")
            self._use_defaults()
        except (OSError, PermissionError):
            print("Could not open JSON file. Using default settings.")
            self._use_defaults()

    def _save_to_file(self) -> None:
        """Save data in the `settings` dict to the JSON file.

        Creates JSON file if it doesn't exist.
        """
        self.file_dir.mkdir(parents=True, exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump(self.settings, f, indent=4)
