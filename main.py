from classes.game import Person, bcolors


# Magic is an array of objects containing different spells that can be called by the player
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 15, "dmg": 140},
         {"name": "Blizzard", "cost": 20, "dmg": 180}]

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
        print("You attacked for", dmg, "points of damage.")
    # if choosing magic, chooses spell and also reduce the cost of the spell from the mp     
    elif index == 1:
        player.choose_spell()
        magic_choice = int(input("Choose Magic:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            # by adding the continue if you don't have enough MP to do a magic attack, you will still be able to go and not skip a turn
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg),  "points of damage" + bcolors.ENDC)

    
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attackcs for", enemy_dmg)

    print("--------------------------")
    print("Enemy's HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)

    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)




    # Checks on the status of HP of player and enemy to determine if the game should keep running 
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You enemy has defeated you!" + bcolors.ENDC)
        running = False
    
    
    
    



