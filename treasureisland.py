print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision = input("You are at a cross road, where do you want to go? Type 'left' or 'right' ")

if decision == "left":
    second_decision = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if second_decision == "wait":
        third_decision = input("You arrive at the island unharmed. There is a house with 3 doors. One 'red', one 'yellow' and one 'blue'. Which color do you choose? ")
        if third_decision == "red":
                print("It is a room full of fire. Game over.")
                quit
        elif third_decision == "yellow":
                print("You have found the treasure. You win!")
                quit
             
        else:
                print("You enter a room full of beasts. You lose.")
                quit
             

    elif second_decision == "swim":
          print("You get attacked by an angry trout. Game over.")
          quit

    else:
        print("invalid input")
elif decision == "right":
      print("You fell into a hole. Game over.")
      quit
     