# def encrypetion(code):
#     if len(code)>3:
#         print(len(code))
#         codeEnc = code[1:]+code[0]
#         codeEnc = "hfg" + codeEnc + "oii"
#         return(codeEnc)
#     else:
#         return(code[::-1])
# encrypt = encrypetion(input("Enter a message for encrypte: "))
# print(encrypt)
def decryption(encrypt):
    if len(encrypt)>3:
        print(len(encrypt))
        enc = (encrypt[3:-3])
        print(enc[-1]+ enc[0:-1])
    else:
        print(encrypt[::-1])
decryption(input())
