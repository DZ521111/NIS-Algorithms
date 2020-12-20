'''
Author : Dhruv B Kakadiya

'''
# Multiplicative Inverse code

# function to find multiplicative Inverse
def find_mul_inverse (a, n):
    t1, t2 = 0, 1
    while(a > 0):
        q = n // a
        r = n - (q * a)
        n, a = a, r
        t = t1 - (q * t2)
        t1, t2 = t2, t 
    gcd, t = n, t1
    return gcd, t

if __name__ == "__main__":
    print("\nEnter the a and mod: \n")
    a, n = map(int, input().split())
    gcd, mul_inverse = find_mul_inverse(a, n)
    if (gcd == 1):
        if (mul_inverse < 0):
            print(f"Multiplicative inverse of {a} modulo {n} is => {mul_inverse % n} and {mul_inverse}\n")
        else:
            print(f"Multiplicative inverse of {a} modulo {n} is => {mul_inverse}\n")
    else:
        print(f"Multiplicative inverse is not possible\n")