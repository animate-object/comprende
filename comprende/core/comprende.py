from comprende.core.types import Module
from comprende.core.important_words import IMPORTANT_WORDS
from typing import List
from enum import Enum

ALL_MODULES: List[Module] = [
    IMPORTANT_WORDS,
]


class ModuleTypes(Enum):
    IMPORTANT_WORDS = IMPORTANT_WORDS

    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return str(self)

    @staticmethod
    def from_string(s: str):
        try:
            return ModuleTypes[s.upper()]
        except KeyError:
            return s
