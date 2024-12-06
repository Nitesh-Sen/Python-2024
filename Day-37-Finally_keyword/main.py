# 
def func1():
    try:
        l = [5, 9, 7, 12, 98]
        i = int(input("Enter the index: "))
        print(l[i])
        return "++++++++ Positive ++++++++"
    except:
        print("Some error occurred")
        return "------- Negative -------"
    finally:
        print("I am always executed.")
    # print("I am always executed.") # If in def condition you get any error. then it will run only except condition and not run any anther direct command. So we can use here "finally" part to execute that in "def" function.
x = func1()
print(x)   