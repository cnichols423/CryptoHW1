# Cohen Nichols
# poly_cipher.py
# hw 1

############################################################################
## algorithm to take txt and encrpyt it
def text_to_cipher(userInput, encryptKey):
    key = list(encryptKey)
    #length of input - length of key
    #append the key at ith pos. mod by length of the key
    for i in range(len(userInput) - len(key)):
        key.append(key[i % len(key)])
    key = "".join(key) #join the new appended key with old key
    cipherText =[]
    #take user input letter by letter and + with the ith pos of key +26
    #then mod the whole thing by 26 to get encrypted letter starting from 'A'
    #add the characters to the array cipherText array and return the char value
    for i in range(len(userInput)):
        a = (ord(userInput[i]) + ord(key[i]) + 26) % 26
        a += ord('A')
        cipherText.append(chr(a))
    return("".join(cipherText))

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

###############################################################################
## end of main
