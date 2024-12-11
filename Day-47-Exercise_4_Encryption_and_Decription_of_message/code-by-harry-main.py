st = input("Enter message: ")
words = st.split(" ")
coding = input("Please choose number 1 for coding or 0 for Decoding: ")
coding = True if (coding == "1") else False
# print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(word)>3): 
            r1 = "ioe"
            r2 = "jfr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print()
    print("Coded message is:", f"\"{" ".join(nwords)}\"")
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print()
    print("De-Coded message is:", f"\"{" ".join(nwords)}\"")