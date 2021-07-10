from classes.game import Person, bcolors


# Magic is an array of objects containing different spells that can be called by the player
magic = [{"name": "Fire", "cost": 10, "dmg": 40},
         {"name": "Thunder", "cost": 15, "dmg": 60},
         {"name": "Blizzard", "cost": 20, "dmg": 80}]

# variables passed to person corresepond to the described persons attributes defined in game
player = Person(460, 80, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

# Bcolors will add color to the script, the ENDC will end the usage of colors in the text
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("========================")
    player.choose_action()
    # input allows for the user to make a choice from the index
    choice = input("Choose Action:")
    # because indexs of arrays start at 0 we need to make a function to eliminate the zero so the proper number corresponds
    index = int(choice) - 1

    # Player choosing to attack enemy
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemey HP:", enemy.get_hp())
    
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attackcs for", enemy_dmg, "Player Hp:", player.get_hp())
    



