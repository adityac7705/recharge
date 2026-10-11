from player import Player
from attack import Attack
from action import Action

player_1 = Player()
player_2 = Player()

guns = Attack("Guns", 1, 10, 1)
fireball = Attack("Fireball", 2, 30, 2)
plasma_beam = Attack("Plasma Beam", 3, 50, 3)

attack_map = {
        Action.GUNS: guns,
        Action.FIREBALL: fireball,
        Action.PLASMA_BEAM: plasma_beam
    }

def get_attack(action):
    return attack_map[action]

def use_attack(player, action):
    attack = get_attack(action)
    return player.spend_charges(attack.cost)

player = Player(charges=2)
print(use_attack(player, Action.FIREBALL))
print(player.charges)

player = Player(charges=1)
print(use_attack(player, Action.FIREBALL))
print(player.charges)