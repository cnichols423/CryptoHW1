# Cohen Nichols
# poly_cipher.py
# hw 1

############################################################################
## algorithm to take txt and encrpyt it
def text_to_cipher(userInput, encryptKey):
    key = list(encryptKey)
    if len(userInput) == len(key):
        return(key)
    else:
        for i in range(len(userInput) - len(key)):
            key.append(key[i % len(key)])
    key = "".join(key)
    cipherText =[]
    for i in range(len(userInput)):
        a = (ord(userInput[i]) + ord(key[i]) + 26) % 26
        a += ord('A')
        cipherText.append(chr(a))
    return("".join(cipherText))

##############################################################################
## take cipher and turn to text
def cipher_to_text(cipherText, key):
    originalText = []
    for i in range(len(cipherText)):
        a = (ord(cipherText[i]) + ord(key[i]) + 26) % 26
        a += ord('A')
        cipherText.append(chr(a))
    return("".join(originalText))

##############################################################################
## main
   
def main():
    print("\n")
    print("showing encyrption")
if __name__ == "__main__":
     main()

userInput = input("enter a message you would like to see encrypted: ")
encryptKey = input("enter the key for encryption: ")


print("\n")
print("encrypted text: ", text_to_cipher(userInput,encryptKey))
