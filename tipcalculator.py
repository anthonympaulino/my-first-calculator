print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How mcuh tip would you like to give? 10, 12 or 15? "))
people_splitting = int(input("How many people will split the bill? "))

tip_amount = bill * (tip_percentage/100)
total_amount = tip_amount + bill
amount_per_person = total_amount / people_splitting
print(f"Each person should pay: ${amount_per_person}")

