# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:46:44 2017

@author: vinntec
"""

class Character():
    """A class to create a character"""

    # Create a character
    def __init__(self, char_name, char_description):
        """Initialise a character with a name and description"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """Describe this character"""
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Returns what the character wants to say"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """Talk to this character"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """Fight with this character"""
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    """A class to create an enemy as a super class of Character"""

    wins = 0 # class variable

    def __init__(self, char_name, char_description):
        """Initialise an enemy with a name and description as a super class of Character"""
        # first make a Character object and then we’ll customise it
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        """Set a weakness for this character"""
        self.weakness = weakness

    def get_weakness(self):
        """Return this character's weakness"""
        return self.weakness

    def set_wins(self):
        """Increments the class variable wins to track the player's successes"""
        Enemy.wins += 1

    def get_wins(self):
        """Returns the current number of wins"""
        return Enemy.wins

    def fight(self, combat_item):
        """Fight with this character. Returns True if the player has won, False otherwise"""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def bribe(self):
        """Bribe an enemy"""
        print("I am vulnerable to", self.weakness)

class Friend(Character):
    """A class to create a friend as a super class of Character"""

    def __init__(self, char_name, char_description):
        """Initialise a friend with a name and description as a super class of Character"""
        # first make a Character object and then we’ll customise it
        super().__init__(char_name, char_description)

    def gift(self):
        """Give a gift to a friend"""
        print("Oh thank-you. I love you!")
