# TredwayP5
# Programmer: Will Tredway (Jaeren William Tredway)
# EMail: jtredway@cnm.edu
# Purpose: make a rock-paper-scissors game that uses
#   a random number generator to pick the computer's 
#   choice, gets the user's choice, reports the winner, 
#   keeps score, and asks the user if they want to 
#   keep playing.

import random

# header for user interface:
print("\n")
print("*"*40)
print("RPS Game : Rock, Paper, Scissors")

#make a list of computer choices:
computer_choices = ['rock', 'paper', 'scissors']

#initialize a list to store the score [user, computer]:
game_score = [0, 0]

#loop the game until the user quits:
game_active = "yes"
user_status = ""
while game_active == "yes" or game_active == "y":
    user_pick = input('\nEnter "rock," "paper," or "scissors":\n').lower()
    
    #check for bad input:
    while user_pick not in computer_choices:
        print("\nBad input, try again:")
        user_pick = input('\nEnter "rock," "paper," or "scissors":\n').lower()
    
    #randomly get the computer's pick:
    random_number = random.randrange(3)
    computer_pick = computer_choices[random_number]
    
    #determine who won:
    if user_pick == "rock":
        if computer_pick == "rock":
            print("Tie game!")
            user_status = "tied"
        elif computer_pick == "paper":
            print("You lost! - paper covers rock")
            game_score[1] += 1
            user_status = "lost"
        elif computer_pick == "scissors":
            print("You won! - rock knocks scissors")
            game_score[0] += 1
            user_status = "won"
    elif user_pick == "paper":
        if computer_pick == "paper":
            print("Tie game!")
            user_status = "tied"
        elif computer_pick == "scissors":
            print("You lost! - scissors cut paper")
            game_score[1] += 1
            user_status = "lost"
        elif computer_pick == "rock":
            print("You won! - paper covers rock")
            game_score[0] += 1
            user_status = "won"
    elif user_pick == "scissors":
        if computer_pick == "scissors":
            print("Tie game!")
            user_status = "tied"
        elif computer_pick == "rock":
            print("You lost! - rock knocks scissors")
            game_score[1] += 1
            user_status = "lost"
        elif computer_pick == "paper":
            print("You won! - scissors cut paper")
            game_score[0] += 1
            user_status = "won" 
    
    #report game score and ask if the user wants to keep playing:
    print(f"You {user_status} that round, the score is: {game_score[0]} - {game_score[1]}.")
    game_active = input("Do you want to play again? (y/n) ").lower()
    if game_active == "no" or game_active == "n": 
        print("\nThanks for playing!")
        quit()