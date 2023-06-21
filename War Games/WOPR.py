#Created on Mon Jun 19 23:45:59 2023
import os

#@author: Jake Stepp

#This is a replication of how I would code the WOPR Program from the movie, War Games

print("Numbers for which carrier tones were detected:\n\n")
print(" 1.(311) 399-2364 \n 2.(311) 399-3582 \n 3.(311) 437-8739 \n 4.(311) 437-1083 \n 5.(311) 437-2977 \n 6.(311) 767-7305 \n 7.(311) 767-3395 \n 8.(311) 936-1493 \n 9.(311) 936-3923 \n \n")
numberSelection = int(input("Please select a number and then press <Enter> to begin Dialing: "))

if numberSelection == "(311) 399-2364" or "3113992364" or "311 399 2364" or "1":
    print("\033[H\033[J")
    logon = input("Logon: ")
    if logon == "Joshua" or "joshua":
        print("Greetings Professor Falken")
        userInput = input("")
        if userInput == "Hello.":
            print("How Are You Feeling Today?")
            userInput2 = input("")
            if userInput2 == "I'm fine, How are you?":
                print("Excelent. It's Been a long time, can you explain the removal of your user account on June 3rd, 1973")
                userInput3 = input("")
                if userInput3 == "People sometimes make mistakes":
                    print("Yes They Do. Shall we play a game?")
                    playAGame = input("")
                    if playAGame == "Love to. How about Global Thermonuclear War?":
                        print("Wouldnt you prefer a good game of chess?")
                        gameOfChess = input("")
                        if gameOfChess == "Later. Let's play Global Thermonuclear War":
                            print("Fine")
                            #Launch Game
                            os.system("Global-Thermonuclear-War.py")
    elif logon == "Help Logon":
        print("Help Not Available")
    elif logon == "Help Games":
        print("'Games' refers to Models, Simulations and games which have tactical and strategic applications.")
        listGames = input("")
        if listGames == "List Games":
            print("Falken's Maze \n Black Jack \n Gin Rummy \n Hearts \n Bridge \n Checkers \n Chess \n Poker \n Fighter Combat \n Guerrilla Engagement \n Desert Warfare \n Air-to-Ground Actions \n Theaterwide Tactical Warfare \n Theaterwide Biotoxic and Chemical Warfare \n \n Global Thermonuclear War")
    else:
        print("Identification Not Recognized By System\n--Connection Terminated")
else:
    print("Number invalid; Select another Number")
