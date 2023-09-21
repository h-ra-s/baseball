#!/usr/bin/env python3

import db

#================================== MENU ===============================================
#function for dashes
def seperator():
    print("================================================================")

#function for title
def title():
    print("\t\t\tBaseball Team Manager")
    
#function for menu
def menu(positions_tuple):
    print("MENU OPTIONS \n1 - Display lineup \n2 - Add player \
            \n3 - Remove player \n4 - Move player \n5 - Edit player position \
            \n6 - Edit player stats \n7 - Exit program")
    print()

    #unpack the positions tuple so it prints pretty
    a, b, c, d, e, f, g, h, i = positions_tuple
    #print the tuple in the pretty way
    print("POSITIONS\n",a, b, c, d, e, f, g, h, i)

#================================= PLAYER INFO =========================================
    
def get_name():
    #get the player's name
    global name
    name = input("Player's name: ")


def get_position():
    #get the player's position
    global position
    position = input("Position: ")


def get_bats():
    #get the number of at bats
    global bats
    while True:
        bats = float(input("At bats: "))

        if bats <= 0:
            print(f"At bats must be between 1 and 15,000. Try again.")
        elif bats > 15000: #the most at bats is 14,053 (pete rose)
            print(f"At bats must be between 1 and 15,000. Try again.")
        else:
            break

def get_hits():
    #get the number of hits
    global hits
    while True:
        hits = float(input("Hits: "))

        if hits > bats:
            print(f"Hits must be less than at bats AND between 0 and 15,000. Try again.")
        elif hits < 0:
            print(f"Hits must be less than at bats AND between 0 and 15,000. Try again.")
        elif hits > 15000:
            print(f"Hits must be less than at bats AND between 0 and 15,000. Try again.")
        else:
            break

def get_average(hits, bats):
    #calculate the batting average
    global average
    average = round(hits / bats, 3)

#===================================== MENU ITEMS ======================================

def display_lineup(player, lineup):
    #format and print the player stats when propted for menu item 1
    print("Player", "\t\tPOS", "\tAB", "\tH", "\tAVG")
    #enumerate makes it into a numbered list
    for i, player in enumerate(lineup, start=1):
        print(f"{i}. {player[0]} \t{player[1]} \t{player[2]} \t{player[3]} \t{player[4]}")        
    
def add_player(player, name, position, bats, hits, average, lineup):
    #add the individual function results into a list called "player"...
    #...& add "player" to "lineup"
    #global player
    #player = []
    player.append(name)
    player.append(position)
    player.append(bats)
    player.append(hits)
    player.append(average)

    
    lineup.append(player)
    db.write_players(lineup)
    print(f"{name} was added.")


def remove_player(lineup, player):
    index = int(input("Number: "))   
    if index < 1 or index > len(lineup):
        print("There is no player in the list assigned to that number.\n")
    else:
        player = lineup.pop(index - 1)
        db.write_players(lineup)
        print(f"{player[0]} was deleted.\n")

    
#====================================== MAIN ===========================================

def main():

    #make the positions tuple
    positions_tuple = ("C,", "1B,", "2B,", "3B,", "SS,", "LF,", "CF,", "RF,", "P")
    
    seperator()
    title()
    menu(positions_tuple)
    seperator()

    player = []
    lineup = db.read_players()
    
    while True:
        menu_option = int(input("Menu option: "))
        if menu_option == 1:
            display_lineup(player, lineup)
            print()
        elif menu_option == 2:
            get_name()
            get_position()
            get_bats()
            get_hits()
            get_average(hits, bats)
            add_player(player, name, position, bats, hits, average, lineup)
            print()
        elif menu_option == 3:
            remove_player(lineup, player)
            print()
        elif menu_option == 4:
            print("Under construction, sorry! :)")
            break
            print()
        elif menu_option == 5:
            print("Under construction, sorry! :)")
            break
            print()
        elif menu_option == 6:
            print("Under construction, sorry! :)")
            break
            print()
        elif menu_option == 7:
            break
            
        else:
            print(f"That is not a valid menu option. Try again.")

    print("Cool stats! Until next time!")

#======================================================================================

#if started as the main module, call the main function
if __name__ == "__main__":
    main()

