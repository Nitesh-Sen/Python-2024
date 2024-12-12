x = 4
print(x)

def helllo():
    x = 5 # this will be change global variable value.
    print(f"The local x is {x}")
    print("Hey, there")
    y = 7 # this is local variable.

print(f"The global x is {x}")
helllo()
print(f"The global x is {x}")