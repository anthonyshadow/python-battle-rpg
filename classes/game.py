import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, def, magic):
       self.maxhp = hp
       self.hp = hp
       self.maxmp = mp
       self.mp = mp
       self.atklow = atk - 10
       self.atkhigh = atk + 10
       self.def = def
       self.magic = magic
       self.actions = ["Attack", "Magic"]
    
    # function to generate how much damage is done by attacks
    def generate_damage(self):
        return random.randrange(self.atklow, self.atkhigh)
    
    # function to generate how much damage is done by spells
    # dmg property comes from the array of objects displaying magical spells, i is the integer in the array which will represent each spell
    def generate_spell_damage(self, i):
        magiclow =self.magic[i]["dmg"] - 5
        magichigh =self.magic[i]["dmg"] + 5
        return random.randrange(magiclow, magichigh)
    
    #  function for player/enemy to take damage
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    
    




