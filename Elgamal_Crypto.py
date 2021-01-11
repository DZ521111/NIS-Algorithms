'''
Author : Dhruv B Kakadiya

'''

from prime_number_generater import simple_testing, miller_rabin_test
# In python there is a module called Elgamal!


if __name__ == "__main__":
    n = int(input("\nEnter the number of bits of prime number :- "))
    while (True):
        n_bit_prime = simple_testing(n)
        if (not miller_rabin_test(n_bit_prime)):
            continue
        else:
            prime = n_bit_prime
            break
    print(f"\nThe prime number is => '{prime}'")