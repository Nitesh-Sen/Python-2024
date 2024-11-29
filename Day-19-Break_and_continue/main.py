for i in range(1, 11):
    print("5 X", i, "=", 5 * i)

print("\n=========> 2nd Loop is Started.<=========")
for i in range(1, 11):
    print("5 X", i, "=", 5 * i)
    if(i == 9): # If i is equal to 9 then this will break the loop and mark it complete.
        break

print("\n========> 3rd Loop is Started <========")
for i in range(1, 13):
    if (i==11):
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5*i)
