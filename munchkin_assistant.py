#Source: https://github.com/Isaaker/Munchkin-Assistant
import time
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
players = input ("Number of players: ")
playersloop = 0
playersusr = players
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
            if playersloop <= players:
                print("Hello")
                playersloop += 1
            if playersloop == players:
                print ("cw")
                break
        if loop == ("b"):
            print ("Thanks for use our program")
            time.sleep(5)
            exit()
            
if version == ("b"):
    print ("Not avaible")
