from math import floor
from random import randint 

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dices = sorted([randint(1, 6) for _ in range(0, 4)])[1:]
        return sum(dices)

def modifier(mod):
    return floor((mod - 10) / 2)