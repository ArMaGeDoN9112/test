for n in range(1, 100000):
    x = bin(n)[2:]
    bin7 = bin(7)[2:]
    bin5 = bin(5)[2:]
    if n % 6 == 0:
        x += bin7
    else:
        x += '1'

    if int(x, 2) % 3 == 0:
        x += bin5
    else:
        x += '1'

    res = int(x, 2)
    if res > 300000:
        print(n)