a = input("Enter the number of Table: ")
print(f"Multiplication table of {a} is: ")
i = 1
# b = type(a).__name__
# print(b)
if a.isdigit():
    print("you are in if part===========>")
    for i in range(11):
        print(f"{int(a)} X {i} = {int(a)*i}")

# else a.isdecimal():
else:
    print("you are in else part============>")
    for i in range(11):
        print(f"{float(a)} X {i} = {float(a)*i}")
