# class Person:
#     name = "Hamaan"
#     occupation = "Scientist"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
# p = Person()
# p.info()

# p.name = "Suman"
# p.occupation = "Teacher"

# p.info()


# 2nd
class Persion:
    def __init__(self):
        print("Hey I am a Person")
a = Persion()

print()
class Percia:
    def __init__(self, nr, ro):
        print("Hey I am a persiion")
        self.name = nr
        self.occ = ro
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Percia("Jerry", "Doctor")
b = Percia("Riya", "Assistent")
print()
a.info()
b.info()