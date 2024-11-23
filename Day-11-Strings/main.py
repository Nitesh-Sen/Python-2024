# Initialize a string variable
name = "Neon"

# Print the entire string
print(name)

# Access and print individual characters of the string by their index
print(name[0])  # First character: 'N'
print(name[1])  # Second character: 'e'
print(name[2])  # Third character: 'o'
print(name[3])  # Fourth character: 'n'

# Attempting to access an index out of range will throw an error
# print(name[4])  # Uncommenting this line will throw an IndexError

# Use a for loop to iterate over each character in the string and print it
print("\nLets use a for loop:")
for c in name: 
    print(c)
print()

# Initialize another string variable
Address = "India"

# Print the string
print(Address)
print()

# Define a string with newline characters (\n) to format the text
apple = 'He said, \nHi Neon \nHow are you?'

# Print the formatted string
print(apple)
print()

# Use triple quotes to define a multiline string
repple = '''He said,
Hi Neon 
Hey I am good.
"I want to see movie"'''

# Print the multiline string
print(repple)
print()

# Use escape characters to include quotes within a string
test = "Hi my name is Neon and I am from \"India\""

# Print the string with escaped quotes
print(test)
print()