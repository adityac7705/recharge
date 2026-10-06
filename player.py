from dataclasses import dataclass

@dataclass
class Player:
    hp : int = 100
    charges : int = 0
    overcharged : bool = False
    shield_available : bool = True

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def charge(self):
        if self.overcharged:
            return False
        elif self.charges == 3:
            self.take_damage(30)
            self.overcharged = True
        else:
            self.charges += 1

    def spend_charges(self, amount):
        if amount <= 0:
            return False
        if self.charges >= amount:
            self.charges -= amount
            return True
        return False