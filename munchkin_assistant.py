#Source: https://github.com/Isaaker/Munchkin-Assistant
import time
def charity():
    cards = input ("How many cards do you have?")
    if cards == ("5"):
        print ("Your turn is over")
    if cards <= ("5"):
        print ("Your turn is over")
    if cards >= ("5"):
        cards2 = input ("Are you the lowest level person or do you tie? [Y / N] ")
        if cards2 == ("y"):
            print ("Discard excess cards")
            print ("Your turn is over")
        if cards2 == ("n"):
            print ("Give the excess cards to the person with the lowest level or tied players.")
            print ("Your turn is over")
def combat():
    while True:
        print ("Compare the total level of all monsters with the total of your level with bonus (if someone helps you their level and bonus also add up)")
        combat1 = input ("Can you defeat the monster? [y/n] ")
        if combat1 == ("y"):
            print ("You killed the monster, level up and take the treasures face down (face up if they helped you).")
            charity()
        if combat1 == ("n"):
            combat2 = input ("Can you flee? [y/n] ")
            if combat2 == ("y"):
                print ("Those who flee must roll the dice")
                combat3 = input ("You have scored more than 5 or 5 [+] or less than 5 [-].")
                if combat3 == ("+"):
                    print ("You have escaped")
                    charity()
                if combat3 == ("-"):
                    print ("You suffer from the bad vibes, although there may be several bad vibes")
                    charity()
            if combat2 == ("n"):
                print ("Ask another player for help, only one player can help you, so choose wisely.")
def findproblems():
    efec
print ("    Munchkin-Assistant    ")
print (" ")
print (" ")
print ("Created by: Isaac Hernán")
print ("Powered by: Python 3")
print ("Hosted  by: GitHub")
print ("License by: Creative Commons")
print ("")
print ("Initializing...")
time.sleep(5)
print ("Select Muchkin Version:")
print ("A. Munchkin Classic")
print ("B. Munchkin Dungeon")
print ("-----------")
version = input ("")
if version == ("a"):
    print ("Munchkin classic selected")
    while True:
        print ("A. Continue the game")
        print ("B. Finish the Game")
        loop = input("")
        if loop == ("a"):
            print ("Take a card")
            time.sleep(5)
            ismonster = input ("Is a monster? [y/n] ")
            if ismonster == ("y"):
                print ("Is a monster")
                combat()
                break
            if ismonster == ("n"):
                curse = input ("Is a curse? [y/n] ")
                if curse == ("y"):
                    print ("The curse affects you")
                    findproblems()
                if curse ("n"):
                    print ("Keep the card in your hand or put it in play right now")
                    findproblems()
                
        if loop == ("b"):
            print ("Thanks for use our program")
            time.sleep(5)
            exit()
            
if version == ("b"):
    print ("Not avaible")
