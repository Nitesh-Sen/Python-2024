def average(a=1, b=11):
    print("The average is ", (int((a+b)/2)))
    print("The average is ", (int((a+b)/2)), "\n")

average(4, 5)
average()
average(5)
average(b=3)


# Function 2nd
def averagE(a, b, c=1):
    print("The average is", (a+b+c)/2)
averagE(5,6)

def average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    print("Average is:", sum/len(number))
average(5, 6, 7)