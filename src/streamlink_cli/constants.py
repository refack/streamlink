from __future__ import annotations

import os
import tempfile
from pathlib import Path

from streamlink.compat import is_darwin, is_win32


DEFAULT_STREAM_METADATA = {
    "id": "Unknown ID",
    "title": "Unknown Title",
    "author": "Unknown Author",
    "category": "No Category",
    "game": "No Game/Category",
}

PROGRESS_INTERVAL_NO_STATUS = 2

CONFIG_FILES: list[Path]
PLUGIN_DIRS: list[Path]
LOG_DIR: Path

xdg_config_home = os.environ.get("XDG_CONFIG_HOME")
xdg_data_home = os.environ.get("XDG_DATA_HOME")
xdg_state_home = os.environ.get("XDG_STATE_HOME")
if is_win32:
    win_app_data = Path(xdg_config_home or os.environ.get("APPDATA") or Path.home() / "AppData")
    CONFIG_FILES = [
        win_app_data / "streamlink" / "config",
    ]
    PLUGIN_DIRS = [
        win_app_data / "streamlink" / "plugins",
    ]
    LOG_DIR = Path(xdg_state_home or os.environ.get("LOCALAPPDATA") or tempfile.gettempdir()) / "streamlink" / "logs"
elif is_darwin:
    darwin_config_home = Path(xdg_config_home or Path.home() / "Library" / "Application Support" / "streamlink")
    CONFIG_FILES = [
        darwin_config_home / "config",
    ]
    PLUGIN_DIRS = [
        darwin_config_home / "plugins",
    ]
    LOG_DIR = Path(xdg_state_home or Path.home() / "Library" / "Logs") / "streamlink"
else:
    posix_config_home = Path(xdg_config_home or "~/.config").expanduser()
    posix_data_home = Path(xdg_data_home or "~/.local/share").expanduser()
    posix_state_home = Path(xdg_state_home or "~/.local/state").expanduser()
    CONFIG_FILES = [
        posix_config_home / "streamlink" / "config",
    ]
    PLUGIN_DIRS = [
        posix_data_home / "streamlink" / "plugins",
    ]
    LOG_DIR = posix_state_home / "streamlink" / "logs"

STREAM_SYNONYMS = ["best", "worst", "best-unfiltered", "worst-unfiltered"]
STREAM_PASSTHROUGH = ["hls", "http"]


__all__ = [
    "CONFIG_FILES",
    "DEFAULT_STREAM_METADATA",
    "LOG_DIR",
    "PLUGIN_DIRS",
    "PROGRESS_INTERVAL_NO_STATUS",
    "STREAM_PASSTHROUGH",
    "STREAM_SYNONYMS",
]
