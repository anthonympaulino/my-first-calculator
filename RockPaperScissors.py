import random

def get_choices() :
    output = input("Enter a choice(rock,paper,scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    dict = {"player" : output , "computer" : computer_choice }
    return dict


choices = get_choices()

def check_wins(player, computer):
    print(f"You chose {player} and computer chose {computer}.")
    if player == computer:
        print("It is a draw.")
    elif player == "scissors" :
        if computer == "paper" :
            return "Scissors cut paper. You win!"
        else :
            return "Rock smashes scissors. You lose."
    elif player == "paper" :
        if computer == "scissors" :
            return "Scissors cuts paper. You lose."
        else :
            return "Paper covers rock. You win!"
    elif player == "rock" :
        if computer == "paper" :
            return "Paper covers rock. You lose."
        else :
            return "Rock smashes scissors. You win!"
    
result = check_wins(choices["player"] , choices["computer"])
print(result)