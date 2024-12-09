a = input("Enter the number of Table: ")
print(f"Multiplication table of {a} is: ")
# b = type(a).__name__
# print(b)
if a.isdigit():
    print("you are in if part===========>")
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")

# else a.isdecimal(): # This can be also happen
else:
    print("you are in else part============>")
    for i in range(1, 11):
        print(f"{float(a)} X {i} = {float(a)*i:.2f}")
        # print(f'{float(a)} X {i} = {float(a)*(i)}')


# Another Program::======================>>>>
# We can use this program when we don't want to stop our program with error in one command or any case. 
# If trriger any error. Than we can just print the error or any output and continue other program without any interption.
# So now we are going to use for this Try and except condition.

b = input("Enter the Another number: ")
print(f"Multiplication table of Antoher number {b} is: ")

if b.isdigit():
    print("you are in if part of another program===========>")
    for i in range(1, 11):
        print(f"{int(b)} X {i} = {int(b)*i}")
# else a.isdecimal():
else:
    print("you are in else part of another program============>")
    for i in range(1, 11):
        # print(f"{float(b)} X {i} = {float(b)*i:.2f}")
        ans = round(float(b) * float(i), 4)
        # print(f"{ans:.4f}")
        print(f"{b} X {i} = {ans:.4f}")

#========================================================
b = input("Enter the Another number: ")
print(f"Multiplication table of Antoher number {b} is: ")
try: 
    if b.isdigit():
        print("you are in if part of another program===========>")
        for i in range(11):
            print(f"{int(b)} X {i} = {int(b)*i}")

    # else a.isdecimal():
    else:
        print("you are in else part of another program============>")
        for i in range(11):
            print(f"{float(b)} X {i} = {float(b)*i:.2f}")
# except Exception as e:
#     print(e)
except:
    print(f"Invaild input {b}!!!!")
#====================================================
#########################################################
# We can also use this for handling the specific error.
# and I have commented these below lines because these both work at same time. but not working with above "except" condtion.
# except IndexError:
#     print("IndexError")
# except ValueError:
#     print("Number entered is not an integer.")
############################################################

print("\nSome line of another code.\nEnd of program")