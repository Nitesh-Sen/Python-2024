marksS = [43, 54, 56, 4, 435, 34]

index = 0
for mark in marksS:
    print(mark)
    if index == 3:
        print(f"Veryy... BAD {mark}")
    index +=1
print("\n\nAnother One ======>")

# Another One
for index, mark in enumerate(marksS):
    print(mark)
    if index == 3:
        print(f"Veryy... BAD {mark}")
print("\n\nNext One =====>")

#Next One
for index, dark in enumerate(marksS, start=1):
    print(f"{index}. {dark}")
          