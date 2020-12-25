'''
Author : Dhruv B Kakadiya

'''
# Multiplicative Cipher

# static variable
mod = 26

from multiplicative_inverse import find_mul_inverse

# function for encryption of plain_text
def mul_cipher_encryption (plain_text, key):
    encrypted_text = ""
    for letter in plain_text:
        if (letter.isupper()):
            encrypted_text += chr(((ord(letter) - 65) * key) % mod + 65)
        elif (letter.islower()):
            encrypted_text += chr(((ord(letter) - 97) * key) % mod + 97)
        else:
            encrypted_text += letter
    return encrypted_text

# function for decryption
def mul_cipher_decryption (encrypted_text, mul_inverse):
    decrypted_text = ""
    for letter in encrypted_text:
        if (letter.isupper()):
            decrypted_text += chr(((ord(letter) - 65) * mul_inverse) % mod + 65)
        elif (letter.islower()):
            decrypted_text += chr(((ord(letter) - 97) * mul_inverse) % mod + 97)
        else:
            decrypted_text += letter
    return decrypted_text

# main function of code
if __name__ == "__main__":
    plain_text = input("\nEnter the plain Text : ")
    key = int(input("\nEnter the Key : "))
    gcd, mul_inverse = find_mul_inverse(key, mod)
    if (gcd == 1):
        encrypted_text = mul_cipher_encryption(plain_text, key)
        print(f"\nThe encrypted text of '{plain_text}' is => '{encrypted_text}'")
        if (mul_inverse < 0):
            mul_inverse = (mul_inverse) % mod
        decrypted_text = mul_cipher_decryption(encrypted_text, mul_inverse)
        print(f"\nThe decrypted text of '{encrypted_text}' is => '{decrypted_text}'")
    else:
        print("\nNot a Valid key!")