'''
Author : Dhruv B Kakadiya

'''
import numpy as np
max_key_length = 9
alphabet = "abcdefghijklmnopqrstuvwxyz"
import random

english_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
				0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
				0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
				0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def vigenere_encryption (plain_text, key):
    plain_text_ord = [ord(letter) for letter in plain_text]
    ascii_key = [ord(letter) for letter in key]
    cipher_text_ord = []
    for i in range(len(plain_text_ord)):
        val = plain_text_ord[i] + ascii_key[i % len(key)] - 97
        if (val > 122):
            cipher_text_ord.append(val - 26)
        else:
            cipher_text_ord.append(val)
    cipher_text = "".join(chr(i) for i in cipher_text_ord)
    return cipher_text

def vigenere_decryption (cipher_text, key):
    cipher_text_ord = [ord(letter) for letter in cipher_text]
    ascii_key = [ord(letter) for letter in key]
    plain_text_ord = []
    for i in range(len(cipher_text_ord)):
        plain_text_ord.append(((cipher_text_ord[i] - ascii_key[i % len(key)]) % 26) + 97)
    plain_text = "".join(chr(i) for i in plain_text_ord)
    return plain_text

def get_ic (cipher_text):
    N = float(len(cipher_text))
    freq_sum = 0.0
    for letter in alphabet:
        freq_sum += cipher_text.count(letter) * (cipher_text.count(letter) - 1)
    ic = (freq_sum) / (N * (N - 1))
    return ic

def find_freq (text):
    N = float(len(text))
    freq = []
    for letter in alphabet:
        freq.append(text.count(letter) / N)
    return freq

def get_key_length (cipher_text):
    all_ic = []
    all_Seq = []
    min, index = 10**3, -1
    for guess_length in range(3, max_key_length):
        ic = 0.0
        avg_ic = 0.0
        for i in range(guess_length):
            sequence = cipher_text[i::guess_length]
            all_Seq.append(sequence)
            ic += get_ic(sequence)
        print(all_Seq)
        avg_ic = ic / guess_length
        all_ic.append(avg_ic)
    print(all_ic)
    guess_1 = all_ic.index(sorted(all_ic, reverse = True)[0]) + 3
    guess_2 = all_ic.index(sorted(all_ic, reverse = True)[1]) + 3
    return guess_1, guess_2

def get_key (cipher_text, key_length):
    max_ = []
    for length in range(key_length):
        result = []
        seq = cipher_text[length::key_length]
        for i in range(26):
            seq_freq = find_freq(seq)
            if (i >= 1):
                seq_freq = seq_freq[i:] + seq_freq[:i]
            mul = [a * b for a, b in zip(seq_freq, english_freq)]
            sum_ = sum(mul)
            result.append(sum_)
        print(result)
        max_.append(result.index(max(result)))
    return max_

if __name__ == "__main__":
    mode = input("\nEnter the mode E -> Encryption and D -> Decryption : ")
    if (mode == "E"):
        plain_text = input("\nEnter the plain text : ")
        plain_text = "".join(letter.lower() for letter in plain_text if letter.isalpha())
        enc_key = input("\nEnter the key :")
        cipher_text = vigenere_encryption(plain_text, enc_key)
        print(f"\nplain text is => '{plain_text}'")
        print(f"\ncipher text is => '{cipher_text}'")
    else:
        cipher_text = input("\nEnter the cipher text : ")
        cipher_text = "".join(letter.lower() for letter in cipher_text if letter.isalpha())
        dec_mode = input("\nEnter 'y' if you have key and 'n' if you haven't : ")
        if (dec_mode == "y"):
            dec_key = input("\nEnter the decryption key : ")
            plain_text = vigenere_decryption(cipher_text, dec_key)
            print(f"\nCipher text is => '{cipher_text}'")
            print(f"\nplain_text is => '{plain_text}'")
        else:
            key_length_1, key_length_2 = get_key_length(cipher_text)
            print(f"\nlenght of key_1 is => '{key_length_1}'")
            print(f"lenght of key_2 is => '{key_length_2}'")
            key_1 = get_key(cipher_text, key_length_1)
            key_2 = get_key(cipher_text, key_length_2)
            print(f"\nthe key_1 is => '{key_1}'")
            print(f"the key_2 is => '{key_2}'")
            #plain_text_1 = vigenere_decryption(cipher_text, key_1)
            #plain_text_2 = vigenere_decryption(cipher_text, key_2)
            #print(f"\nthe plain text for key '{key_1}' is => '{plain_text_1}'")
            #print(f"\nthe plain text for key '{key_2}' is => '{plain_text_2}'")
