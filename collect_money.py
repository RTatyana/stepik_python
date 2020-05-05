for _ in range(int(input())):
    a, b, c, n = map(int, input().split())

    r = (max(a, b, c) - a) + (max(a, b, c) - b) + (max(a, b, c) - c)

    if r > n:
        print('NO')
    else:
        if (n - r) % 3 == 0:
            print('YES')
        else:
            print('NO')
    #
    # l = sorted(a, b, c)
    # # A = max(a, b, c)
    # # B = min(a, b, c)
    # A, B, C = map((l[0], l[1], l[2]))
    # r = A - B
    #
    # if n < r:
    #     print('NO')
    # else:
    #     n = n - r
    #     B = A
    #
    # rr = max()
    #
    # if rr > n:
    #     print('NO')
    # # if rr == n:
    # #     print('YES')
    # if (n - rr) % 3 == 0:
    #     print('YES')
    # else:
    #     print('NO')
    #
    # while a < m and n > 0:
    #     n = n - 1
    #     a = a + 1
    #
    # while b < m and n > 0:
    #     n = n - 1
    #     b = b + 1
    #
    # while c < m and n > 0:
    #     n = n - 1
    #     c = c + 1
    #
    # if n % 3 == 0 and a == b and b == c:
    #     print('YES')
    # else:
    #     print('NO')
