'''
Author : Dhruv B Kakadiya

'''
# import libraries
from multiplicative_inverse import find_mul_inverse
from prime_number_generater import simple_testing, miller_rabin_test

# find power mod prime
def power_nmod (a, n, prime):
    res = 1
    a %= prime
    if (a == 0):
        return (0)
    while (n > 0):
        if ((n & 1) == 1):
            res = (res * a) % prime
        n >>= 1
        a = (a ** 2) % prime
    return (res)

# main if condition
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