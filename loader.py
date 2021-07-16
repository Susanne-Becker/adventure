"""
# -------------------------------------------------------------------------------
# loader.py
# -------------------------------------------------------------------------------
#
# load files
#
# Gemaakt door: Susanne Becker
#
"""

from room import Room
from item import Item
import cs50

# dictionaries
dictionary_synonyms = {}
rooms = {}
items = {}


def load_room_graph(filename):
    # open file
    f = open(filename, "r")
    k = 1

    # read file line by line and make rooms
    while f:
        line = f.readline()
        if line == "\n":
            break
        remove = line.rstrip("\n")
        data = remove.split("\t")
        room = Room(data[0], data[1], data[2])
        rooms[k] = room
        k += 1

    # read file line by line and determine source_room
    while f:
        j = 2
        k = 1
        line = f.readline()
        if line == "\n":
            break
        remove = line.rstrip("\n")
        data = remove.split("\t")
        source_room = rooms[int(data[0])]
        
        # connect directions and direction rooms (pay attention to special connections(conditions))
        for z in data:
            if j >= len(data):
                break
            if "/" in data[j]:
                number = data[j].split("/")
                item_room = rooms[int(number[0])]
                item = number[1]
                destination_item = rooms[int(number[0])]
                direction = data[k]
                source_room.add_condition_item(direction, item)
                source_room.add_condition_direction(direction, destination_item)
            else:
                direction = data[k]
                destination_room = rooms[int(data[j])]
                source_room.add_connection(direction, destination_room)
            j += 2
            k += 2

    # read file line by line and put items in rooms
    while f:
        line = f.readline()
        if line == "":
            break
        remove = line.rstrip("\n")
        data = remove.split("\t")
        items[data[0]] = Item(data[0], data[1], data[2]) 
        room_item = rooms[int(data[2])]
        room_item.items.append(items[data[0]])

    # open synonyms file and put it in synonyms dictionary
    file = open("data/Synonyms.dat", "r")
    while file:
        line = file.readline()
        if line == "":
            break
        remove = line.rstrip("\n")
        s = remove.split("=")
        letter = s[0]
        word = s[1]
        dictionary_synonyms[word] = (word, letter)

    f.close()
    return rooms[1]
