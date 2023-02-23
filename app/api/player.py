from colours import *
from cup import Cup
from die import Die
from helper_functions import roll_die

class Player:
    def __init__(self, name):
        self.name = name
        self.colour = None
        self.cup = None
        self.dice = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def get_cup(self):
        return self.cup

    def set_cup(self, cup):
        self.cup = cup

    def get_dice(self):
        return self.dice

    def select_colour_setup(self, colour, game_colours):
        for i in range(game_colours.colour_count()):
            if (colour == game_colours.colours[i]):
                self.set_colour(colour)
                game_colours.remove_colour(colour)
                self.cup = Cup(self.colour)
                self.get_five_dice()
                return True
            else:
                return False

    def get_five_dice(self):
        for i in range(0,5):
            self.dice.append(Die())
            self.dice[i].set_die_colour(self.colour)

    def get_dice_values(self):
        dice_values = []
        for i in range(self.count_dice()):
            dice_values.append(self.dice[i].get_die_value()) 
        return dice_values
    
    def count_dice(self):
        return int(len(self.dice))

    def roll_dice(self):
        list_of_values = self.dice
        for i in range(self.count_dice()):
            list_of_values[i].set_die_value(roll_die())

    def remove_die(self):
        if (self.count_dice() > 0):
            self.dice.pop()
        else:
            return 0
        
# game_colours = Colours()
# player1 = Player("Chris")
# print(game_colours.get_colours_available())
# print(player1.get_name())
# player1.select_colour_setup("Green")
# print(player1.get_colour())
# print(player1.cup.get_colour_of_cup())
# print(player1.get_dice_values())
# print(player1.count_dice())
# player1.roll_dice()
# print(player1.get_dice_values())
# player1.remove_die()
# print(player1.get_dice_values())
# print(player1.count_dice())
