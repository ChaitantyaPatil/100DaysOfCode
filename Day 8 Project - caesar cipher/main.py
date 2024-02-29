import functions as f
import logo
print(logo.logo)
flag =True
while flag:
    action = input("To encrypt message type 'Encode' to decrypt message type 'Decode': ").lower()
    message = input("Entre your message : ")
    shift = int(input("Entre The shift : "))
    if (action == 'encode'):
        print(f.encrypt(message,shift))
    if (action == 'decode'):
        print(f.decrypt(message,shift))
    ans = input("want to do again ? yes/no : ")
    if (ans== 'no'):
        flag = False
        print("*************** GoodBye **************")

