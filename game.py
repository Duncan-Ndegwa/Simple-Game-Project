

import time
import random


'''
                NOTES TO SELF
- Start with the background processes such as how the winner is determined.
- Then go to the choices made by the computer and the user.
- Then go to the user interaction( Game itself.
- The extra 'print()' are just for spacing to make it neater.

'''




# Background mechanics (How the game works/ How winner is decided)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw!"
    elif (player_choice == "Rock" and computer_choice == "Scissors", "Lizard" or 
         player_choice == "Paper" and computer_choice == "Rock", "Spock" or 
         player_choice == "Scissors" and computer_choice == "Paper", "Lizards" or 
         player_choice == "Lizard" and computer_choice == "Paper", "Spock" or 
        player_choice == "Spock" and computer_choice == "Scossors", "Rock") :
        
        return "Congratulations, You win!"
    else:
        return "Computer wins!"








# Getting the computers chioce from the list

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])





# User interface [Game itself]

def play_game():
    
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    wins = 0
    losses = 0
    draws = 0

    time.sleep(1)

    while True:

        print()

        player_choice = input("Enter Rock, Paper, Scissors, Lizard or Spock (or 'q' to exit): ").capitalize()
        
        if player_choice == 'Q':
            print(f"Final Scores ---> Wins: {wins}, Losses: {losses}, draws:{draws}")
            print()
            print(f"Thanks for playing {total} matches with us today!")
            break
        if player_choice not in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
            print("Invalid choice. Please choose either Rock, Paper, Scissors, Lizard or Spock.")
            continue
        computer_choice = get_computer_choice()
       
        print()
        
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        print()
        
        print(determine_winner(player_choice, computer_choice))
        

        print()


        # TRACKER
        result = determine_winner(player_choice,computer_choice)
        
        
        if result == "Congratulations, You win!":
            wins += 1
        elif result == "Computer wins!":
            losses += 1
        else:
            draws += 1


        total = wins + losses + draws

if __name__ == "__main__":
    play_game()

