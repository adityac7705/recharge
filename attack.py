from dataclasses import dataclass

@dataclass
class Attack:
    name: str
    cost: int
    damage: int
    hierarchy: int