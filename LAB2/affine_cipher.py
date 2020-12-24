'''
Author : Dhruv B Kakadiya

'''
# Multiplicative Cipher
from multiplicative_inverse import find_mul_inverse\

# static variable
mod = 26

# function for Encryption
def affine_cipher_encryption (plain_text, key1, key2):
    encrypted_text = ""
    for letter in plain_text:
        if (letter.isupper()):
            encrypted_text += chr(((ord(letter) - 65) * key1 + key2) % mod + 65)
        elif (letter.islower()):
            encrypted_text += chr(((ord(letter) - 97) * key1 + key2) % mod + 97)
        else:
            encrypted_text += letter
    return encrypted_text

# function for Decryption
def affine_cipher_decryption (encrypted_text, mul_inverse, key2):
    decrypted_text = ""
    for letter in encrypted_text:
        if (letter.isupper()):
            decrypted_text += chr(((ord(letter) - 65 - key2) * mul_inverse) % mod + 65)
        elif (letter.islower()):
            decrypted_text += chr(((ord(letter) - 97 - key2) * mul_inverse) % mod + 97)
        else:
            decrypted_text += letter
    return decrypted_text

# main function of code
if __name__ == "__main__":
    plain_text = input("\nEnter the plain Text : ")
    key1 = int(input("\nEnter the Key1 : "))
    key2 = int(input("\nEnter the Key2 : "))
    gcd, mul_inverse = find_mul_inverse(key1, mod)
    if (gcd == 1):
        encrypted_text = affine_cipher_encryption(plain_text, key1, key2)
        print(f"\nThe encrypted text of '{plain_text}' is => '{encrypted_text}'")
        if (mul_inverse < 0):
            mul_inverse = (mul_inverse) % mod
        decrypted_text = affine_cipher_decryption(encrypted_text, mul_inverse, key2)
        print(f"\nThe decrypted text of '{encrypted_text}' is => '{decrypted_text}'")
    else:
        print("\nNot a Valid key1!")