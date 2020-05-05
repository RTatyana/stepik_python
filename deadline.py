import math

for _ in range(int(input())):
    A = [int(i) for i in input().split()]

    n = A[0]
    d = A[1]

    x1 = 0
    x2 = 0
    discr = (n - 1) ** 2 - 4 * (d - n)

    if discr < 0:
        print('NO')
    elif d <= n:
        print('YES')
    else:
        x1 = round((n - 1 + math.sqrt(discr)) / 2)
        x2 = round((n - 1 - math.sqrt(discr)) / 2)

        if x1 == x2 and x1 > 0:
            if (x1 + round(d/(x1+1))) <= n:
                print('YES')
            else:
                print('NO')

        elif (x1 == 0 and x2 > 0) or (x2 == 0 and x1 > 0):
            if (max(x1, x2) + round(d/(max(x1, x2)+1))) <= n:
                print('YES')
            else:
                print('NO')

        else:
            # X = [int(x) for x in range(min(x1, x2), max(x1, x2)) if x > 0 and (x + round(d/(x+1))) <= n]
            res = 0
            for x in range(min(x1, x2), max(x1, x2)):
                if x > 0 and (x + round(d/(x+1))) <= n:
                    res = 1
                    break
            if res == 1:
                print('YES')
            else:
                print('NO')


