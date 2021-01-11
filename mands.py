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

for i in range(22, 193):
    print(multiply_and_square(22, i, 193))