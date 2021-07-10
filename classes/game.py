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
    
    def generate_damage(self):
        return random.randrange(self.atklow, self.atkhigh)
    
    



