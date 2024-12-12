# # READING A FILE
# f = open('file.txt', 'r') # if you will not add (, "r"). This will auto open in read mood.
# text = f.read() 
# print(text)
# f.close()
# print(f)
# print("Once Again:-", text)

# WRITE A FILE
f = open('file.txt', 'a')
text = f.write('Hello, your text has changed.\n')
f.close()
print(text)

# WRITE OPERATION WITHOUT CLOSE FUNCTION
with open('file.txt', 'a') as f:
    f.write("Hey I am inside the with\n\n")