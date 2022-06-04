import random
from random import randint
import switch as switch

def playGame():
    print("Hello, welcome to the game arena\n The title of this game is Rock-Paper-Scissors\n Game is ON!")
    options = ["R","P","S"]
    while True:
        userInput = input("Select a R,P,S").capitalize()
        computer = random.choice(options)
        if userInput=='R' and computer== 'S':
            print("You win, Rock beats Scissors")
        elif userInput=='R' and computer=='P':
            print("You lose, Paper beats Rock")
        elif userInput=='R' and computer=='R':
            print("It's a tie")
        elif userInput=='P' and computer=='S':
            print("You lose, Scissors beats Paper")
        elif userInput=='P' and computer=='R':
            print("You win, Paper beats Rock")
        elif userInput=='P' and computer=='P':
            print("It's a tie")
        elif userInput=='S' and computer=='S':
            print("It's a tie!")
        elif userInput=='S' and computer=='R':
            print("You lose, Rock beats Scissors")
        elif userInput=='S' and computer=='P':
            print("You win, Scissors beats Paper")
        else:
            print("Select a valid command")
            print("")
            print("R for rock, P for paper,S for scissors.")
playGame()