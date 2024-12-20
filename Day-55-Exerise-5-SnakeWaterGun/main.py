import random
youPoint = botPoint = i = 0
num = 1
print(youPoint, botPoint, i)
while i < 10:
    print(f"\n===============> Game {num} <===============")
    You = input("1. Snake\n2. Water\n3. Gun\nChoose a number in [1-3]: ")
    if not You.strip():
        print("Value is empty. Try Again...!")
    elif You.isdigit():
        You = int(You)
        if 0 < You < 4:
            i = i + 1
            num = num + 1
            print(f"You Choose: {You}")
            Bot = random.randint(1,3)
            print(f"Bot Choose: {Bot}")
            if You is Bot:
                print("Draw.")
            elif You == 1 and Bot == 2 or You == 2 and Bot == 3 or You == 3 and Bot == 1:
                print("You Win..!")
                youPoint = youPoint + 1
            elif You == 1 and Bot == 3 or You == 2 and Bot == 1 or You == 3 and Bot == 2:
                print("You Loose..!")
                botPoint = botPoint + 1
        else:
            txt = ("Invalid Input...! -------> Try Again <---------")
            txt = txt.center(150)
            print(txt)
    else:
        print("Invalid input. Please enter valid Number.")


print("\n")
print("Final is ==============>")
if botPoint == youPoint:
    print(f"Game is Draw..............!\nYour Point is: {youPoint}\nBot Point is: {botPoint}")
elif botPoint > youPoint:
    print(f"You loose the Game............!\nYour Point is: {youPoint}\nBot Point is: {botPoint}")
else:
    print(f"You win the Game............!\nYour Point is: {youPoint}\nBot Point is: {botPoint}")