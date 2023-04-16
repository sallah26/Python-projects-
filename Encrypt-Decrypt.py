alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encrypt():
    str2=str(input("Enter the text to encript : "))
    shift=int(input("Enter the amount of shift to shift the given text: "))
    let=""
    for i in range(len(str2)):
        ke=str2[i]
        possition=alpha.index(ke)
        possition=int(possition)
        new_possition=alpha[possition+shift]
        let+=new_possition
    print("Encrypted text is: ",let)
def decrypt():
    str1=str(input("Enter the text to decript : "))
    shift=int(input("Enter the amount of shift to shift the given text: "))
    let=""
    for i in range(len(str1)):
        ke=str1[i]
        possition=alpha.index(ke)
        possition=int(possition)
        new_possition=alpha[possition-shift]
        let+=new_possition
    print("Decrypted text is: ",let)
direction=str(input("Enter \n1. to decript the given text, and \n2. to encription of given text \n choose: "))
if(direction=="1"):
    encrypt()
else:
    decrypt()