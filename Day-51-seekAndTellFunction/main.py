# SEEK AND TELL FUNCTION
with open('filee.txt') as f:
    print(type(f))
    f.seek(10) #Move to the 0th byte in the file
    print(f.tell()) # this will show you until byte you have seeked. In-Short: this will print your seek value.
    data = f.read(5) # Read the next 5 bytes
    print("This is 5 byte after 10 byte of file filee.txt:", f"\"{data}\"")

# TRUNCATE FUNCTION
with open('test-file.txt', 'w') as f:
    f.write("Hello Universe")
    f.truncate(9) # If you will comment this line. Then you will get all text ("Hello Universe") in you file.
with open('test-file.txt', 'r') as f:
    print(f.read())


