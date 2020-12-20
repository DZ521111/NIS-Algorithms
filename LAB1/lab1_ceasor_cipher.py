'''
Author : Dhruv B Kakadiya

'''
# Additive Cipher Algorithm or Ceasor Cipher Algorithm

mod = 26
# encryption function for encrypt the plain text into the cipher text
def encryption (plain_text, key):
    encrypted_text = ""
    for letter in plain_text:
        if (letter.isupper()):
            encrypted_text += chr((ord(letter) - 65 + key) % mod + 65)
        elif (letter.islower()):
            encrypted_text += chr((ord(letter) - 97 + key) % mod + 97)
        else:
            encrypted_text += letter
    return encrypted_text

# depcryption function for decode the encrypted text
def decryption (encrypted_text, key):
    decrypted_text = ""
    for letter in encrypted_text:
        if (letter.isupper()):
            decrypted_text += chr((ord(letter) - 65 - key) % mod + 65)
        elif (letter.islower()):
            decrypted_text += chr((ord(letter) - 97 - key) % mod + 97)
        else:
            decrypted_text += letter
    return decrypted_text

# crypt analysis function for attackers to find the appropriate text matching
def crypt_analysis (encrypted_text):
    try_match_text_list = []
    for key in range(1, 26):
        try_match_text = ""
        for letter in encrypted_text:
            if (letter.isupper()):
                try_match_text += chr((ord(letter) - 65 - key) % mod + 65)
            else:
                try_match_text += chr((ord(letter) - 97 - key) % mod + 97)
        try_match_text_list.append(try_match_text)
    return try_match_text_list

if __name__ == "__main__":
    plain_text = input("\nEnter the plain text : ")
    key = int(input("\nEnter the encryption key : "))
    cipher_text = encryption(plain_text, key)
    print(f"\nplain text is => {plain_text}")
    print(f"\nThe cipher text is => {cipher_text}")
    decrypted_text = decryption(cipher_text, key)
    print(f"\nAfter the decryption the text is => {decrypted_text}")
