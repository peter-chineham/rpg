# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:28:25 2017

@author: vinntec
"""
class Item():
    """A class to create an item"""

    def __init__(self, name):
        """Initialise an item with a name"""
        self.name = name
        self.description = None

    # Describe this item
    def describe(self):
        """Describe this item"""
        print("The item " + self.name + " is here!")
        print(self.description)

    def get_name(self):
        """Return the name of this item"""
        return self.name

    def set_name(self, item_name):
        """Set the name of this item"""
        self.name = item_name

    def get_description(self):
        """Return the description of this item"""
        return self.description

    def set_description(self, item_description):
        """Set a description of this item"""
        self.description = item_description
