from classes.game import Person, bcolors


# Magic is an array of objects containing different spells that can be called by the player
magic = [{"name": "Fire", "cost": 10, "dmg": 40},
         {"name": "Thunder", "cost": 15, "dmg": 60},
         {"name": "Blizzard", "cost": 20, "dmg": 80}]

# variables passed to person corresepond to the described persons attributes defined in game
player = Person(460, 80, 60, 34, magic)

