print("\n======> Type 1.0 <=======")
a = 8
b = 8
gmean = int((a*b)/(a+b))
print(gmean)

c = 7
d = 6
gmean2 = int((a*b)/(a+b))
print(gmean2)

print("\n======> Type 1.1 <========")
def calculateGmean(a, b):
    mean = float((a*b)/(a+b)) # You will get answer in float not integer.
    print(mean)

c = 2
d = 9
calculateGmean(c,d)
a = 3
b = 5
calculateGmean(a,b)

print("\n=========> Type 2.0 <===========")
a = 9
b = 9
if(a>b):
    print(a, "is greater than", b)
else:
    print(a, "is less than or equal", b)

print("\n=========> Type 2.1 <===========")
def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("First number is small or equal")
e = 14
f = 17
isGreater(e, f)

def isLessor(a, b):
    pass # This functino is not complete and after write pass this will no throw any error.

print("\n=========> Type 3.0 <===========")
def names(Fname, Sname):
    print("Hello,", Fname, "and", Sname)

names("AWS", "Google")