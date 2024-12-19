class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee =>  {self.id} is {self.name}")


e1 = Employee("Rohan Naag", 347)
e1.showDetails()
e2 = Employee("Thinos", 75)
e2.showDetails()

class Programmer(Employee):
    def showLanguage(self):
        print("Python is really Awsome!!!\n")

print()
e4 = Programmer("Riyad", 12)
e4.showLanguage()