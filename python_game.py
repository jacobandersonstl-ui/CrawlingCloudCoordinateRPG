#Python game
print("Welcome to Python Game 1! This is my first Python based game made with ZERO plugins/libraries and made all by myself. I've made games before, though they were not good. This source code is 100 percent open source and can be legally reposted, as long as I (fives9335) am credited.")

#   PATCH NOTES
#   * Added health
#   * added potions
#   * added potion pickups
#   * increased map size from 6x6 to 12x12
#   * AND MORE!!!



#!--IMPORTANT--! Legend:
#           N, E, S, W = Cardinal Directions
#           2, 2 = Camp
#           ???, ??? = Exit
#           12 Moves to Exit = Golden Run!


































input("\nPress Enter to Start!")

print("Starting...")


x = 0
y = 0
moves = 0
has_map = False
health = 100
potions = 1
potion_locations = [[-3, -1], [7, 9]]
maps_at_camp = 5
is_god = False
steampowered = False
Steampowerd_Protocol = False

while True:
    if has_map == False:
        print("Current Location: ???, ???. Moves: ", moves, "Health: ", health, "Potions: ", potions)
    if has_map == True:
        print("Current location: ", x, ",", y, "Moves = ", moves, "Health: ", health, "Potions: ", potions)
    move = input("Where do you want to go? N, E, S, W, H to use a potion (make sure you have some first!), or Q to Quit: ").upper().strip()

    if move == "N":
        print("Ok! Going North!")
        y += 1
        moves += 1
    elif move == "E":
        print("Ok! Going East!")
        x += 1
        moves += 1
    elif move == "S":
        print("Ok! going South!")
        y -= 1
        moves += 1
    elif move == "W":
        print("Ok! Going West!")
        x -= 1
        moves += 1
    elif move == "H":
        if potions > 0 and health < 100:
            input("\nYou used 1 potion. +15 Health.")
            potions -= 1
            health = health + 15
            if health > 100:
                health = 100
        elif potions <= 0:
            input("\nOh No! You have no potions! Go searching around for some!")
    elif move == "Q":
        print("Ok! Bye!")
        quit()
    else:
        if has_map == False:
            print("You trip on a root as a consequence of not having your map of the woods with you. You get back up to continue your search to find your way out of the labyrinth that is this damned forest!")
        elif has_map == True:
            input("\nYou look around yourself, unsure of where you are. You check your map, and realize you'll be okay, you'll make it home!")
    
#EVENTS

    if x == 1 and y == 3 and moves <= 6:
        input("\n!--EVENT--! WOAH! You found a treasure chest! oh man! it's empty :(")
    elif x == 1 and y == 3 and moves > 6:
        input("\n!--EVENT--! You found a *Treasure Chest*!! You got 5 potions!")
        potions += 5
    
    if x == -2 and y == 3:
        input("\n!--EVENT--! HOLY CRAP!! A STORM!! WE BETTER GET OUTA HERE! (press Enter)")
        if has_map == True:
            input("\nYou run North, WOAH! You're at 5, 5 on the map!")
        elif has_map == False:
            input("\nYou got thrown by the whipping wind! Where are you now?")
        x = 5
        y = 5

    if x == 3 and y == 1 and moves > 5:
        if has_map == True:
            input("\n!--EVENT--! A bandit stole your map! Head back to camp to get a new one!")
            has_map = False
        elif has_map == False:
            pass #I will add an event with time

    if x == -3 and y == -1 and [-3, -1] in potion_locations:
        input("\nYou found a potion! Great work!")
        input("\n1 Potion added to bag.")
        potions += 1
        potion_locations.remove([-3, -1])
    elif x == 7 and y == 9 and [7, 9] in potion_locations:
        input("\nYou found a potion! Great work!")
        input("\n1 Potion added to bag.")
        potions += 1
        potion_locations.remove([7, 9])
    
    if x == 9 and y == 4 and moves == 12:
        input("\n!--EVENT--! A bandit has attacked you! -30 Health!")
        health -= 30
        if has_map == False:
            input("\nThat darned bandit looked like he was looking for a map of the forest! Luckily you don't have one, so he leaves you alone!")
        if has_map == True:
            input("That bandit! He took your map!")
            has_map = False

    if health <= 0:
        input("\nYou blacked out from losing too much blood. Let's get you back to camp!")
        input("\n50 health restored.")
        health = 50
        x = 0
        y = 0
        moves = 0

#   STEAMPOWERED PROTOCOL

    if is_god == True and Steampowerd_Protocol == True and steampowered == True:
        source = input("\nSource: ").upper().strip()
        input("\nSTEAMPOWERED PROTOCOL ACTIVE")
        health = 100
        potions = 100
        moves = 12
        has_map = True
        if source == "VALVE":
            x = 6
            y = 6
        elif source == "MACHINE":
            x = 0
            y = 0
            moves = 0
            has_map = False
            potions = 1
            health = 100
            is_god = False
            steampowered = False
            Steampowerd_Protocol = False


    

































#Map
    if x == 2 and y == 2 and has_map == False:
        if maps_at_camp <= 0:
            input("\nYou're out of maps at camp!")
        elif maps_at_camp >= 0:
            input("\nYou return to the camp, ready to collect your map!")
            input("\nYou Found: MAP")
            has_map = True
            maps_at_camp -= 1






        #cheat
    if move == "FIVES9335_DEV":
        x = 6
        y = 6
        has_map = True
        moves = 12
    
    if move == "FIVES9335_HEALTH_0":
        health = 0
    
    if move == "FIVES9335_MAX_HP":
        health = 100
    
    if move == "FIVES9335_GOD_MODE":
        potions = 1000
        has_map = True
        health = 100
        if health >= 0:
            health = 100
    
    if move == "FIVES9335_STEAMPOWERED":
        input("INITIATING: STEAMPOWERED PROTOCOL")
        has_map = True
        is_god = True
        steampowered = True
        Steampowerd_Protocol = True



#Win

    moves_to_win = (moves == 12)
    winning_spot = (x == 6 and y == 6)

    if winning_spot:
        if moves_to_win:
            input("\nPERFECT SCORE! YOU MADE IT TO THE EXIT IN JUST 12 MOVES!! GOOD JOB!")
        elif moves > 12:
            input("\nYou WIN!")
            
        restart = input("\nPress R and then Enter to restart!").upper().strip()

        if restart == "R":
            moves = 0
            x = 0
            y = 0
            has_map = False
            health = 100
            potions = 0
            maps_at_camp = 5
        else:
            moves = 0
            x = 0
            y = 0
            has_map = False
            health = 100
            potions = 0
            maps_at_camp = 5


