class Employee:
    def __init__(self):
        self.__name = "Nitesh Sen"

a = Employee()
# print(a.__name) # Cannot be accessed directly
print(a._Employee__name) # Can be accessed indirectly