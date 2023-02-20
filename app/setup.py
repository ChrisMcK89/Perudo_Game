from player import Player

class Setup:

    def __init__(self):
        self.players = []
        self.starting_total_die = len(self.players) * 5
        self.cups = len(self.players)

    def get_players(self):
        return self.players
    
    def get_player_name(self, player_number):
        player = self.players[player_number - 1]
        player_name = player.get_name()
        return player_name

    def get_starting_total_die(self):
        return self.starting_total_die

    def get_cups(self):
        return self.cups

    def add_player(self, player):
        self.players.append(player)

# create player
player1 = Player()
player1.set_name("Chris")
player1.set_cup("Red")
player1.set_die("4")

# initiate setup
game1 = Setup()

# add player to game
game1.add_player(player1)

# check player added to game
player1_name = game1.get_player_name(1)
print(player1_name)




