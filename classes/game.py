import random
from unicodedata import name



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
    def __init__(self, name, hp, mp, atk, defence, magic, items):
       self.maxhp = hp
       self.hp = hp
       self.maxmp = mp
       self.mp = mp
       self.atklow = atk - 10
       self.atkhigh = atk + 10
       self.defence = defence
       self.magic = magic
       self.items = items
       self.actions = ["Attack", "Magic", "Items"]
       self.name = name
    
    # function to generate how much damage is done by attacks
    def generate_damage(self):
        return random.randrange(self.atklow, self.atkhigh)
    
    #  function for player/enemy to take damage
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg):
        self.hp +=dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
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

    # def get_spell_name(self, i):
    #     return self.magic[i]["name"]

    # def get_spell_mp_cost(self, i):
    #     return self.magic[i]["cost"]
    
    # Function to allow user to choose action
    def choose_action(self):
        i = 1
        print("\n" + "    "  +bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1
    
    # Function to choose spell to use and how much mp it uses
    def choose_magic(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    # Function to choose Items
    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    Items" +bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name, ":", item["item"].description, " (x" + str(item["quantity"]) +")")
            i += 1
    
    # Function for player stats
    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        
        while len(hp_bar) < 25:
            hp_bar += " "
        
        mp_bar = ""
        mpbar_ticks = (self.mp / self.maxmp) * 100 / 10

        while mpbar_ticks > 0:
            mp_bar += "█"
            mpbar_ticks -= 1
        
        while len(mp_bar) < 10:
            mp_bar += " "
        
        # chp = self.hp 
        # shp = ""
        # if len(chp) < 4:
        #     while len(shp) < len(chp) - 4:

        print("                    _________________________                 __________ ")
        print(bcolors.BOLD + self.name +"    "+
              str(self.hp) + "/" + str(self.maxhp) +" |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|       "+
              str(self.mp) + "/" + str(self.maxmp) +"   |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")







    
    




