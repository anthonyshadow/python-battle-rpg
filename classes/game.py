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

    # Utility functions
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp

    # function that reduces mp when magic spells are used
    def reduce_mp(self, cost):
        self.mp -= cost
    
    # function that tells user what spell they have chosen
    def get_spell_name(self, i):
        return self.magic[i]["name"]
    
    # function that gets spells mp cost
    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
    
    # Function to allow user to choose action
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
    
    # Function to choose spell to use and how much mp it uses
    def choose_spell(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["mp"]) + ")")
            i += 1







    
    




