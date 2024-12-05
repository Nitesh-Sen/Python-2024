def fib(n):
    a, b = 0, 1
    # a = 0
    # b = 1
    # print(a, end=" ")
    # print(b, end=" ")
    # a = b + a
    for i in range(n): 
        # yield  a
        print(a, end=" ")
        # a = b # not working in fibonicci
        # b = a+b # not working in fibonicci
        a, b = b, a + b
        # print(a, end=" ")
        # b = a
        # a = b + a
fib(10)