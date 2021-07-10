from classes.game import Person, bcolors
from classes.magic import Spell

#Black magic spells
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 8, 80, "black")
blizzard = Spell("Blizzard", 14, 140, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

# White magic spells
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")



# variables passed to person corresepond to the described persons attributes defined in game
player = Person(460, 80, 60, 34, [fire, thunder, blizzard, meteor, quake, cure, cura])

enemy = Person(1200, 65, 45, 25, [])

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
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            # by adding the continue if you don't have enough MP to do a magic attack, you will still be able to go and not skip a turn
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "Heals for ", str(magic_dmg), "HP" +bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),  "points of damage" + bcolors.ENDC)

    
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
    
    
    
    



