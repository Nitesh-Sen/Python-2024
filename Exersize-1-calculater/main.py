# Python program for simple calculator
# Function to add 2 numbers
def add(nu1, nu2):
  return nu1 + nu2

# Function to subtract 2 numberss
def subtract(nu1, nu2):
  return nu1 - nu2

# Function to multiply 2 numbers
def multiply(nu1, nu2):
  return nu1 * nu2

# Function to dvide 2 numbers
def divide(nu1, nu2):
  return nu1 / nu2

print("Please select operation:\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n")

# Take input from the user
select = int(input("Select operations from 1, 2, 3, 4: "))

print()

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select ==1:
  print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select ==2:
  print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
  print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif select == 4:
  print(number_1, "/", number_2, "=", divide(number_1, number_2))

else: 
  print("Invalid Input")
