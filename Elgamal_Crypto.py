'''
Author : Dhruv B Kakadiya

'''

import random as rd
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

# phi function
def phi (n):
    return (n - 1)

# multiply and square function
def multiply_and_square(a, x, n):
    x = bin(x)
    x = x[2 : ]
    x = x[:: -1]
    y = 1
    for i in range(0, len(x)):
        if (int(x[i]) == 1):
            y = (y * a) % n
        a = (a ** 2) % n
    return y

# find order
def primitive_roots_order (prime):
    order = [None] * prime
    # find the all primitive roots
    for r in range(1, prime):
        first_one = True
        for c in range(1, prime):
            mas = multiply_and_square(r, c, prime)
            if ((first_one) and (mas == 1)):
                order[r] = c
                first_one = False
    return order

# find all primitive roots
def all_roots (order, prime):
    proots = []
    phi_prime = phi (prime)
    for i in range(1, len(order)):
        if (order[i] == phi_prime):
            proots.append(i)
    return proots

# find public and private keys
def find_public_private_key (proots, prime):
    e1 = proots[rd.randint(0, len(proots) - 1)]
    condition = prime - 2
    while (True):
        d = proots[rd.randint(0, len(proots) - 1)]
        if (d <= condition):
            break
    e2 = multiply_and_square (e1, d, prime)
    return (e1, e2, prime), d

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

    order = primitive_roots_order (prime)
    proots = all_roots (order, prime)

    # finding public and private key
    public_key, private_key = find_public_private_key (proots, prime)
    print(public_key, private_key)






