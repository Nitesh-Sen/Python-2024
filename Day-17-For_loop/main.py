name = 'Nitesh Sen'
for i in name:
    print(i, end=", ") # It will print horizontel
print("\n")
for i in name:
    print(i) # It will print vertical
    if(i == "e"):
        print("This is something special.")

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

print("\n")
for a in range(1, 100000001):
    print(a)

for se in range(1, 50, 3): # there third element is showing gap in 3 for every number and print that.
    print(se) 