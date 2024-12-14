# def duble(x):
#     return x*2
duble = lambda x: x*2
print(duble(8))

cube = lambda x: x*x*x
avg = lambda x, y: (x+y)/2
avgOfThree = lambda x, y, z: (x+y+z)/3
print(cube(7))
print(avg(8, 14))
print(avgOfThree(1, 8, 9))

def apple(fx, value):
    return 6 + fx(value)

print(apple(cube, 3))
print(apple(lambda x: x*x*x, 3))