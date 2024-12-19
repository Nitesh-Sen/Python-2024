class MClass:
    def __init__(self, value):
        self._value = value 

    def show(self):
        print(f"Value is {self._value}")

    # @property
    # def ten_value(self):
    #     return str(self._value) + str(self._value)
    @property
    def ten_value(self):
        return 100 * self._value
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

# obj = MClass(1010)
# print(obj._value)
# print(obj.ten_value)
obj = MClass(101)
print(obj._value)
print(obj.ten_value)

# Use Setter....>
print()
obj.ten_value = 10101
print(obj.ten_value)
obj.show()
