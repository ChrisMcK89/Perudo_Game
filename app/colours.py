class Colours:
    def __init__(self):
        self.colours = ["Black", "Blue", "Orange", "Red", "Yellow", "Green"]

    def get_colours_available(self):
        return self.colours

    def colour_count(self):
        return int(len(self.colours))

    def remove_colour(self, colour_to_remove):
        list_copy = self.colours
        remove_count = list_copy.count(colour_to_remove)
        for i in range(remove_count):
            list_copy.remove(colour_to_remove)
        self.colours = list_copy


# colours = Colours()
# print(colours.get_colours_available())
# colours.remove_colour("Blue")
# print(colours.get_colours_available())