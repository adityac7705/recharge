from player import Player

player_1 = Player()
player_2 = Player()

print(player_1.spend_charges(0))
print(player_1.spend_charges(-1))
player_1.charge()
print(player_1)
print(player_1.spend_charges(3))
print(player_1)
print(player_1.spend_charges(1))
print(player_1)