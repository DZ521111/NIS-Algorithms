'''
Author : Dhruv B Kakadiya

'''

from prime_number_generater import simple_testing, miller_rabin_test
# In python there is a module called Elgamal!

# to find multiplicative_inverse
def find_mul_inverse (a, n):
    mod = n
    t1, t2 = 0, 1
    while(a > 0):
        q = n // a
        r = n - (q * a)
        n, a = a, r
        t = t1 - (q * t2)
        t1, t2 = t2, t
    return (t1 % mod)


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