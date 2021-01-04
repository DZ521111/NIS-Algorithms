'''
Author : Dhruv B Kakadiya

'''
# import functions from prime number generater
from prime_number_generater import simple_testing, miller_rabin_test

# function multiplicative inverse
def find_mul_inverse (a, n):
    t1, t2 = 0, 1
    while(a > 0):
        q = n // a
        r = n - (q * a)
        n, a = a, r
        t = t1 - (q * t2)
        t1, t2 = t2, t
    gcd, t = n, t1
    return (t % n)

#generate_keys
def generate_keys ():
    pass

# main method
if __name__ == '__main__':
    count = 0
    primes = []
    n = int(input("\nEnter the number of bits of prime number :- "))
    while (count < 2):
        n_bit_prime = simple_testing(n)
        if (not miller_rabin_test(n_bit_prime)):
            continue
        else:
            primes.append(n_bit_prime)
            count += 1
    p, q = primes
    print(f"\nThe primes are => {p}")
    print(f"\nThe primes are => {q}")

    public_key, private_key = generate_keys (p, q)

    # rsa implementation

