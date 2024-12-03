import time
a = int(time.strftime("%H"))
name = "Nitesh Sen"
if(0 >=  a < 12):
    print("Good Morning", name)
elif(a < 17):
    print("Good Afternoon", name)
elif(a < 21):
    print("Good Evening", name)
else:
    print("Good Night", name)

