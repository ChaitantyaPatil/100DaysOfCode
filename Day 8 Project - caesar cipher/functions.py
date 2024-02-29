alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(message, shift):
    cipher = ""
    for letter in message:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift) % 26
            cipher += alphabet[index]
        else:
            cipher += letter
    
    return cipher

def decrypt(message, shift):
    cipher = ""
    for letter in message:
        if letter in alphabet:
            index = (alphabet.index(letter) - shift) % 26
            cipher += alphabet[index]
        else:
            cipher += letter
    
    return cipher