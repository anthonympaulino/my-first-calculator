print(f"How old will you be by the end of 2024?")
age = input(" ")
age = int(age)

if type(age) == int:
    birth_year = 2024 - age
    print(f"You were born in the year {birth_year}.")
    if age > 17:
        print("You are an adult.")
    else:
        print("You are still a child.")
else:
    print(f"Wrong input. Type the age in digits.")
    quit



