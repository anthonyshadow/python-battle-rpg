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
    def __init__(self, hp, mp, atk, defence, magic):
       self.maxhp = hp
       self.hp = hp
       self.maxmp = mp
       self.mp = mp
       self.atklow = atk - 10
       self.atkhigh = atk + 10
       self.defence = defence
       self.magic = magic
       self.actions = ["Attack", "Magic"]
    
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
    
    # Function to allow user to choose action
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
    
    # Function to choose spell to use and how much mp it uses
    def choose_magic(self):
        i = 1

        print(bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1







    
    




