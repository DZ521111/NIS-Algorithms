'''
Author : Dhruv B Kakadiya

'''
# import libraries
from multiplicative_inverse import find_mul_inverse

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

