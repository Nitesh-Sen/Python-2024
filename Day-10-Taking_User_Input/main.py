# Take an input from the user and print it
a = input()
print(a)

# Prompt the user to enter their name and print it
a = input("Enter Your Name: ")
print(a)

# Prompt the user to enter a number and display it as their "lucky number"
b = input("Enter any number: ")
print("Your Lucky number is", b)

# Initialize variables for numeric inputs
u = 1
w = 2

# Prompt the user to enter a number (can include decimal values)
u = float(input("Enter 1st Number: "))  # Accepts decimal values

# Prompt the user to enter another number (only integer values are valid)
w = int(input("Enter Second Number: "))  # Converts input to an integer

# Subtract the second number from the first and display the result
print(u - w)