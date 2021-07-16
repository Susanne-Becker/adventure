"""
# -------------------------------------------------------------------------------
# adventure.py
# -------------------------------------------------------------------------------
#
# adventure game
#
# Gemaakt door: Susanne Becker
#
"""

import loader
from room import Room
from item import Item


class Adventure():

    # Create rooms and items for the game that was specified at the command line
    def __init__(self, filename):
        self._current_room = loader.load_room_graph(filename)
        self.player_items = []
        self.synonyms = loader.dictionary_synonyms

    # Pass along the description of the current room, be it short or long
    def room_description(self):
        return self._current_room.description()

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        if self._current_room.has_condition(direction) == True:
            for index in range(len(self.player_items)):
                if self._current_room.get_condition_item(direction) in self.player_items[index].item:
                    self._current_room = self._current_room.get_condition_direction(direction)
                    return True
        if self._current_room.has_connection(direction) == True:
            self._current_room = self._current_room.get_connection(direction)
            return True
        else:
            return False


if __name__ == "__main__":

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python3 adventure.py [name]")
        exit(1)

    # Load the requested game or else Tiny
    print("Loading...")
    if len(argv) == 2:
        game_name = argv[1]
    elif len(argv) == 1:
        game_name = "Tiny"
    filename = f"data/{game_name}Adv.dat"

    # Create game
    adventure = Adventure(filename)

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.room_description())
    adventure._current_room.set_visited()

    while True:
        # check if room has connection with "FORCED", otherwise you ask user input
        if adventure._current_room.has_connection("FORCED"):
            adventure._current_room.set_unvisited()
            command = "FORCED"
        else:
            command = input("> ").upper()
            word = command.split()

        # implement synonyms
        for index in adventure.synonyms:
            if command == adventure.synonyms[index][1]:
                command = adventure.synonyms[index][0]

        # Perform the move or other command
        if adventure.move(command) == True:
            print(adventure.room_description())
            adventure._current_room.set_visited()
            if adventure._current_room.items:
                for index in range(len(adventure._current_room.items)):
                    print(f'{adventure._current_room.items[index].item}: {adventure._current_room.items[index].description}')

        # invalid command
        elif adventure.move(command) != True and word[0] != "TAKE" and word[0] != "DROP" and word[0] != "HELP" and word[0] != "LOOK" and word[0] != "INVENTORY":
            print("Invalid command.")

        # take items, check if item in current room
        if word[0] == "TAKE" and adventure._current_room.items:
            for index in range(len(adventure._current_room.items)):
                if word[1] == adventure._current_room.items[index].item:
                    adventure.player_items.append(adventure._current_room.items.pop(index))
                    print(f"{word[1]} taken")
                    break
                else:
                    print("No such item")

        # no items in current room
        elif word[0] == "TAKE" and len(adventure._current_room.items) < 1:
            print("No such items")
        
        # drop item, check if item in inventory
        if word[0] == "DROP" and adventure.player_items:
            for index in range(len(adventure.player_items)):
                if word[1] == adventure.player_items[index].item:
                    adventure._current_room.items.append(adventure.player_items.pop(index))
                    print(f"{word[1]} dropped")
                    break
                else:
                    print("No such item")

        # no items in inventory
        elif word[0] == "DROP" and len(adventure.player_items) < 1:
            print("No such items")
            
        # command HELP
        if word[0] == "HELP":
            print("You can move by typing directions such as EAST/WEST/IN/OUT \nQUIT quits the game. \nHELP prints instructions for the game. \nLOOK lists the complete description of the room and its contents. \nINVENTORY lists all items in your inventory.")

        # command LOOK
        if word[0] == "LOOK":
            adventure._current_room.set_unvisited()
            print(adventure.room_description())
            if adventure._current_room.items:
                for index in range(len(adventure._current_room.items)):
                    print(f'{adventure._current_room.items[index].item}: {adventure._current_room.items[index].description}')

        # command INVENTORY
        if word[0] == "INVENTORY":
            if adventure.player_items:
                for index in range(len(adventure.player_items)):
                    print(f'{adventure.player_items[index].item}: {adventure.player_items[index].description}')
            else:
                print("Your inventory is empty")

        # Allows player to exit the game loop
        if command == "QUIT":
            break
