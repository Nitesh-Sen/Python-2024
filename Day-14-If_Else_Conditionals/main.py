a = int(input("Enter Your Age: "))
print("\n<==============>\nYou are", a, "year old. \nBye, Have a nice day\n<==============>")

# Conditional Operator
# >, <, >=, <=, ==
if(a>18):
    print("You can widhrow money from your account.")
else:
    print("You cann't widhrow money from your account")

applePrice = int(input("Enter price of apple /KG: "))
budget = int(input("Enter your budget: "))
if(applePrice <= budget):
    print("Alexa, Add apple in cart.\nYeah..! you can buy apples")
else:
    print("Alexa, Don't add apple in cart.")
salary = budget
#New condition
a = int(((salary - applePrice)/salary) * 100)
print(a, "\n")
if(a >= 80):
    print("You can buy easily.")
elif(a >= 60):
    print("it's okay you can buy.")
elif(a >= 40):
    print("It is more than half of your salary.")
else:
    print("Don't Buy.")

if(a >= 40):
    if (a <= 60):
        print("it's okay you can buy.")
    elif (a <= 80):
        print("You can buy easily.")
    else:
        print("buy buy buy")
else:
    print("Don't Buy.")