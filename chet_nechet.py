for _ in range(int(input())):
    a, b = map(int, input().split())

    k = 0
    diff = 0

    if a == b:
        k = 0
    if b > a:
        diff = b - a
        if diff % 2 == 0:
            k = 2
        else:
            k = 1
    if a > b :
        diff = a - b
        if diff % 2 == 0:
            k = 1
        else:
            k = 2
    print(k)
