for _ in range(int(input())):
    x, y, a, b = input().split()

    n = (int(y) - int(x)) / (int(a) + int(b))
    if n.is_integer():
        print(int(n))
    else:
        print(-1)
