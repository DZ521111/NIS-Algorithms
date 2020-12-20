'''
Author : Dhruv B Kakadiya

'''
# Substitution Cipher Algorithm or Monoalphabetic Cipher Algorithm

Organized_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shuffled_key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt_decrypt_text(input_text, key, mode = None):
    converted_text = ""
    org = Organized_key
    shuff = key
    if (mode == "decryption"):
        org, shuff = shuff, org
    for letter in input_text:
        if (letter.upper() in org):
            if (letter.isupper()):
                converted_text += shuff[org.find(letter.upper())].upper()
            else:
                converted_text += shuff[org.find(letter.upper())].lower()
        else:
            converted_text += letter
    return converted_text

if __name__ == "__main__":
    input_text = input("\nEnter the text : ")
    print("\n1. encryption\n2. decryption")
    mode = input("\nchoose mode : ")
    if (mode == "encryption"):
        result = encrypt_decrypt_text(input_text, shuffled_key, mode)
    else:
        result = encrypt_decrypt_text(input_text, shuffled_key, mode)
    print(f"\nthe input text is => {input_text}")
    print(f"\nAfter the mode => '{mode}' the text is => '{result}'")
