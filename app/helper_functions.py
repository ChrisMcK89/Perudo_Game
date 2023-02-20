import random

def roll_die():
    return random.randint(1,6)





def get_player_details(player):
    print(player.name)
    print(player.colour)
    print(player.cup.get_colour_of_cup())
    print(player.count_dice())
    print(player.get_dice_values())
    