a = 4
b = "4"
print(a is b) # Exact location of object in memory
print(a == b) # value

print()
a = [1, 3, 64]
b = [1, 3, 64]
print(a is b) 
print(a == b)

print()
a = 3
b = 3
print(a is b) 
print(a == b)

print()
a = "jam"
b = "jam"
print(a is b)
print(a == b)

print()
a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)
print(a == b)

print()
a = None
b = None
print(a is b)
print(a == b)
print(a is None)
