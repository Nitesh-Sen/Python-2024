#################### MAP ##################
from functools import reduce


cube = lambda x: x*x*x
l = [1, 2, 3, 4, 5, 6, 7]
# lisOf = []
# for item in l:
#      lisOf.append(cube(item))
# print(lisOf)

#SHORT-WAY
# lisOf = list(map(cube, l))
# print(lisOf)
print(list(map(cube, l)))

################## Filter ########################
def filter_function(a):
    return a>4
print(list(filter(filter_function, l)))

############### Reduce ###################
print(reduce(lambda x,y: x+y, l))