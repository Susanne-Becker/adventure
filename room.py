"""
# -------------------------------------------------------------------------------
# room.py
# -------------------------------------------------------------------------------
#
# make rooms, connections, conditions
#
# Gemaakt door: Susanne Becker
#
"""

import cs50


class Room():
    # objects that are stored in particular rooms
    def __init__(self, room, name, long_description):
        self.room = room
        self.name = name
        self.long_description = long_description
        self.flag = False
        self.connection = {}
        self.items = []
        self.condition_direction = {}
        self.condition_item = {}
    
    # mark room as visited
    def set_visited(self):
        self.flag = True
        
    # mark room as unvisited
    def set_unvisited(self):
        self.flag = False

    # show description of room depending on visited or not
    def description(self):
        if self.flag == True:
            return self.name
        else:
            return self.long_description

    # add connection between rooms
    def add_connection(self, direction, room):
        self.connection[f"{direction}"] = room
        
    # get the connection at the direction entered
    def get_connection(self, direction):
        return self.connection[f"{direction}"]
        
    # check if direction has a connection
    def has_connection(self, direction):
        if direction in self.connection:
            return True
        else:
            return False
    
    # connection between rooms with items
    def add_condition_item(self, direction, item):
        self.condition_item[f"{direction}"] = item
    
    # connection between rooms by direction
    def add_condition_direction(self, direction, destination):
        self.condition_direction[f"{direction}"] = destination
        
    # get the connection at the direction entered
    def get_condition_item(self, direction):
        return self.condition_item[f"{direction}"]
    
    # get the connection at the direction entered
    def get_condition_direction(self, direction):
        return self.condition_direction[f"{direction}"]
      
    # check if direction has a connection  
    def has_condition(self, direction):
        if direction in self.condition_item:
            return True
        else:
            return False
