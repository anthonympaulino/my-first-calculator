print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Welcome to the game!")
    print(" Let's begin")

score = 0
answer = input("What is CPU in full? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is ROM in full? ")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is RAM in full? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is PSU in full? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is GPU in full? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

print(f"total score: str({score}/5)")

if score > 4:
    print(f"Excellent score!")
elif score < 2:
    print(f"Try harder")
else:
    print(f"fairly done")





          
# use the formatted string well otherwise you have to resort to concantenation