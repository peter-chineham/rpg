# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:54:44 2017

@author: vinntec
"""
class Room():
    """A class to create a room"""

    def __init__(self, room_name):
        """Initialise a room with a name"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def get_name(self):
        """Return the name of the room"""
        return self.name

    def set_name(self, room_name):
        """Set the name of the room"""
        self.name = room_name

    def get_description(self):
        """Return a description of the room"""
        return self.description

    def set_description(self, room_description):
        """Set a description of the room"""
        self.description = room_description

    def get_character(self):
        """Return the character in this room or None"""
        return self.character

    def set_character(self, character):
        """Set the character in this room"""
        self.character = character

    # getters and setters for item
    def get_item(self):
        """Return the item in this room or None"""
        return self.item

    def set_item(self, item):
        """Set the item in this room"""
        self.item = item

    def describe(self):
        """Describe this room"""
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Link this room to another one by direction"""
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """Print details of this room"""
        print(self.name)
        print("-----------")
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """Move from this room to another - if valid"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
