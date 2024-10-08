from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    asset_location: str = Path("src/midi_web_app/application/assets")
    screen_size: tuple = (1600, 1200)
