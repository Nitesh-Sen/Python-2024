# Strings are immutable in Python
c = "!..Neon!..!"

# Get the length of the string
print(len(c), "\n")

# Convert all characters to uppercase
print(c.upper())  # Output: "!..NEON!..!"

# Convert all characters to lowercase
print(c.lower())  # Output: "!..neon!..!"

# Remove trailing "!" characters (does not affect leading "!" characters)
print(c.rstrip("!"))  # Output: "!..Neon!.."

# Replace "neon" with "newn" (case-sensitive, so this won't work as 'n' is lowercase)
print(c.replace("neon", "newn"))  # Output: "!..Neon!..!"

# Replace "Neon" with "newN" (case-sensitive, so this will work)
print(c.replace('Neon', "newN"))  # Output: "!..newN!..!"

# Redefine the string
c = "!..NeoN..! !..RocK..! !..JacK..!"

# Split the string into a list using spaces as the delimiter
print(c.split(" "))  # Output: ['!..NeoN..!', '!..RocK..!', '!..JacK..!']
