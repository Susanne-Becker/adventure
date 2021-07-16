"""
# -------------------------------------------------------------------------------
# item.py
# -------------------------------------------------------------------------------
#
# store items
#
# Gemaakt door: Susanne Becker
#
"""


class Item():
    # objects of the items
    def __init__(self, item, description, room_nr):
        self.item = item
        self.description = description
        self.room_nr = room_nr

