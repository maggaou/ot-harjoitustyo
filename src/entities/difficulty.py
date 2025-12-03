from enum import StrEnum


class Difficulty(StrEnum):
    """Liikkeen vaikeusaste."""
    
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
