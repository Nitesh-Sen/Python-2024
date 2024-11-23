# Strings are immutable in Python
c = "!..Neon!..!"

# Get the length of the string
print(len(c), "\n")

# Convert all characters to uppercase
print(c.upper()) 

# Convert all characters to lowercase
print(c.lower())  

# Remove trailing "!" characters (does not affect leading "!" characters)
print(c.rstrip("!"))

# Replace "neon" with "newn" (case-sensitive, so this won't work as 'n' is lowercase)
print(c.replace("neon", "newn"))  

# Replace "Neon" with "newN" (case-sensitive, so this will work)
print(c.replace('Neon', "newN"))  

# Redefine the string
c = "!..NeoN..! !..RocK..! !..JacK..!"

# Split the string into a list using spaces as the delimiter
print(c.split(" ")) 
