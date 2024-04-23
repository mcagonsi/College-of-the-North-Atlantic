from dataclasses import dataclass


@dataclass
class Preferences:
    name: str = ''
    language: str = ''
    saveTime: int = 0
