a = (input("Choose any option between a to d: "))
if not a in ("a, b, c, d"):
    raise ValueError("======> Choose the given value a to d only <======")
else: 
    print(f"Hey..!, You choose => {a}")