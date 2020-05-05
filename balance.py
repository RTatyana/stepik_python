for _ in range(int(input())):
    n = int(input())

    p = []
    a = 0
    b = 0

    b1 = 0

    for i in range(1, n + 1):
        p.append(2 ** i)
    p.reverse()
    a = a + p[0]

    for i in range(1, len(p)):
        if a > b and b1 < n//2:
            b = b + p[i]
            b1 += 1
        else:
            a = a + p[i]

    print(abs(a - b))
