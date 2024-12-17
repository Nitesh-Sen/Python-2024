class Person:
    name = "Shivam Thakre"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Riyan Gupta"
a.occupation = "Software Engineer"
# print(a.name, a.occupation)
a.info()