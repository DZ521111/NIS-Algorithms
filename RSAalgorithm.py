'''
Author : Dhruv B Kakadiya

'''
# import functions from prime number generater
from prime_number_generater import simple_testing, miller_rabin_test
from math import gcd

# function multiplicative inverse
def find_mul_inverse (a, n):
    t1, t2 = 0, 1
    while(a > 0):
        q = n // a
        r = n - (q * a)
        n, a = a, r
        t = t1 - (q * t2)
        t1, t2 = t2, t
    t = t1
    return (t % n)

# find phi of prime number n => n - 1 ; n is prime
def phi (n):
    return (n - 1)

# encryption function
def encryption (plain_text, e, n):
    pass

# decryption function
def decryption (cipher_text, d, n):
    pass

#generate_keys
def generate_keys (p, q):
    for e in range(2, phi(p) * phi(q)):
        gcd_ = gcd(e, phi(p) * phi(q))
        if (gcd_ == 1):
            break
    d = find_mul_inverse(e, phi(p) * phi(q))
    public_key = (e, p * q)
    private_key = (d, p * q)
    return public_key, private_key

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

    # rsa implementation
    public_key, private_key = generate_keys (p, q)
    e, n = public_key
    d, n = private_key
    print(e, n)
    print(d, n)



