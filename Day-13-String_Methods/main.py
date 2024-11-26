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

blogHeading = "introduction tO Js:"
print(blogHeading.capitalize())

word = "Welcome in my world"
print(len(word))
print(word.center(50))
print(len(word.center(50)))

print(c.count("NeoN"))

nu = "Welcome to console !!!"
print(nu.endswith("!!!"))

sentence = "Hello everyone, there is ns."
print(sentence.find("isan"))
# print(sentence.index("isah")) # this will find given word if that will not found. it will throw error and script will be stop.

sentence = "We wish you Happy Birthday"
print(sentence.isprintable())

sentence = "We wish you Happy Birthday\n"
print(sentence.isprintable())

sentence = "Hi, How are you?"
print(sentence.title())