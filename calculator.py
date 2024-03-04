print("What do you want to calculate today?")
print("The format x (operation) y is used")
x = int(input("x = "))
y = int(input("y = "))
print("what operation do you want to perform on the two numbers?")
operation = input(" ")
if operation == "*":
    print(x * y)
elif operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "/":
    print(x / y)
else:
    print("invalid input!")
             
