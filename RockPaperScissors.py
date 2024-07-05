import random
computer_options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(computer_options)
print("Welcome to the RockPaperScissors game!")
player_choice = input("choose A for Rock B for Paper and C for Scissors: ")
A = "Rock" 
B = "Paper"
C = "Scissors"
if player_choice == "A":
    if computer_choice == "Rock":
        print(f"You chose {A} and computer chose Rock.")
        print("It is a tie.")
    elif computer_choice == "Paper":
        print(f"You chose {A} and computer chose Paper.")
        print("You lose.")
    else:
        print(f"You chose {A} and computer chose Scissors.")
        print("You win!")

elif player_choice == "B":
    if computer_choice == "Rock":
        print(f"You chose {B} and computer chose Rock.")
        print("You win!")
    elif computer_choice == "Paper":
        print(f"You chose {B} and computer chose Paper.")
        print("It is a tie.")
    else:
        print(f"You chose {B} and computer chose Scissors.")
        print("You lose.")

elif player_choice == "C":
    if computer_choice == "Rock":
        print(f"You chose {C} and computer chose Rock.")
        print("You lose.")
    elif computer_choice == "Paper":
        print(f"You chose {C} and computer chose Paper.")
        print("You win!")
    else:
        print(f"You chose {C} and computer chose Scissors.")
        print("It is a tie")

else:
    print("Invalid response. Choose between A, B and C")