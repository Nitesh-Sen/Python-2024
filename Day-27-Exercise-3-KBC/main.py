import time, sys, fontstyle

def animate_text(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

text = (fontstyle.apply('Welcome in KBC', 'bold/Italic/red/GREEN_BG'))
animate_text( text, 0.05)
tr = 0
for i in range(2): 
    output = input("Do you want to continue to play. Press (Y/n): ")
    if output in ("y", "Y"):
        print("you have pressed:", output)
        # break
        a = (input("Q1. How many Days in a Year? \n1. 31\n2. 90\n3. 180\n4. 365\nPress number in 1 to 4: "))
        if a in ("4"):
            animate_text("You earned 10 Lakh ruppes. There is your next question:- \n", 0.05)
            a = (input("Q2. What AWS service is used to create and manage virtual private networks (VPNs) in the cloud?\n1. Amazon EC2\n2. AWS Direct Connect\n3. Amazon VPC\n4. Amazon Route 53\nPress number in 1 to 4: "))
            if a in ("3"):
                animate_text(("Congrats....!!!, You earned 30 Lakh rupees. There is your next Question:- \n"), 0.05)
                a = (input("Q3. Which AWS service can be used to distribute content globally and improve website performance?\n1. Amazon CloudFront\n2. AWS Glacier\n3. AWS Snowball\n4. Amazon Route 53\nPress number in 1 to 4: "))
                if a in ("1"):
                    animate_text("Congratulations....!!!, You earned 1 Crore rupees and KBC has done....;)", 0.05)
                    break
                else:
                    print("\nWrong Answer, you have earned 30 Lakh Rupees only.")
                break
            else:
                print("\nWrong Answer, you have earned 10 Lakh Rupees only.")
                break
        else:
            print("\nWrong Answer you have earned 0 Rupees.")
            break
        
    elif output in ("n", "N"):
        print("You have pressed oposite: ", output)
        break
    else:
        if (i == 1):
            print("You given wrong input two times. Program is going to stop, Bye :(")
            break
        else:
            print("wrong input.!!!. Try Again.")
            continue

    
