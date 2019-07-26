from classes.game import Person, bcolors
import random


magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(160, 65, 60, 34, magic)
enemy = Person(250, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

print("===========================================")
print(bcolors.OKGREEN + bcolors.BOLD + "STATS PLAYER:" + bcolors.ENDC)
print("Health:", player.get_max_hp())
print("Magic Points:", player.get_max_mp())
print("Average Attacking Power:", (player.atkh + player.atkl) / 2)
print("===========================================")
print(bcolors.FAIL + bcolors.BOLD + "STATS ENEMY:" + bcolors.ENDC)
print("Health:", enemy.get_max_hp())
print("Magic Points:", enemy.get_max_mp())
print("Average Attacking Power:", (enemy.atkh + enemy.atkl) / 2)


while running:
    print("===========================================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1
    print("You chose", choice, player.actions[index])

    # Player Attacks
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attack with", dmg, "damage.")
        # print("The Enemy has now", enemy.get_hp(), "health.")

    elif index == 1:
        player.choose_magic()
        choice_magic = input("Choose Magic:")
        index_magic = int(choice_magic) - 1
        print("You chose", choice_magic, player.get_spell_name(index_magic))
        dmg = player.generate_spell_damage(index_magic)
        enemy.take_damage(dmg)
        print("You attack with", dmg, "spell damage.")
        # print("The Enemy has now", enemy.get_hp(), "health.")
        player.reduce_mp(player.get_spell_mp_cost(index_magic))
        # print("You have now", player.get_mp(), "mp left.")
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "YOU WON THE GAME" + bcolors.ENDC)
        break

    # Enemy Attacks
    print("Now the enemy attacks")
    action_enemy = random.randint(0, 1)
    if action_enemy == 0:
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print("The enemy attacks with", dmg, "damage.")
        # print("You have now", player.get_hp(), "health.")

    elif action_enemy == 1:
        chosen_spell_enemy = random.randint(0, 2)
        print("The enemy chose the Magic", player.get_spell_name(chosen_spell_enemy))
        dmg = enemy.generate_spell_damage(chosen_spell_enemy)
        player.take_damage(dmg)
        print("You were attack by the enemy with", dmg, "spell damage.")
        # print("You have now", player.get_hp(), "health left.")
        player.reduce_mp(player.get_spell_mp_cost(chosen_spell_enemy))
    if player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "YOU LOST THE GAME" + bcolors.ENDC)
        running = False

    print("===========================================")
    print(bcolors.OKGREEN + bcolors.BOLD + "STATS PLAYER:" + bcolors.ENDC)
    print("Health:", player.get_hp())
    print("Magic Points:", player.get_mp())
    print("===========================================")
    print(bcolors.FAIL + bcolors.BOLD + "STATS ENEMY:" + bcolors.ENDC)
    print("Health:", enemy.get_hp())
    print("Magic Points:", enemy.get_mp())

