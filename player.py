from dataclasses import dataclass

@dataclass
class Player:
    hp : int = 100
    charges : int = 0
    overcharged : bool = False
    shield_available : bool = True

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        