def decorator(Gmx):
    def Gfx(*args, **kwargs):
        print("\n\nHey, there......................\\")
        Gmx(*args, **kwargs)
        print("...Bye, Bye!!!")
    return Gfx

@decorator
def hello():
    print("Hello Universe")

def add(a, b):
    print(a + b)

hello()
decorator(add)(1,2)


