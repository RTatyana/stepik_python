import math

for _ in range(int(input())):
    n = int(input())

    flag = True
    simple = True

    if n < 24:
        flag = False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                simple = False
                break

    if flag is False or simple is True:
        print('NO')
    else:
        for i in range(2, int(n // 4)):
            if n % i == 0:
                a = i
                n = int(n / i)

                for j in range(a + 1, int(n // 2)):
                    if n % j == 0:
                        b = j
                        c = int(n / j)

                        if c != b and a != c:
                            print('YES')
                            print(a, b, c)
                            flag = True
                            break
                        else:
                            flag = False

                    else:
                        flag = False
            if flag is True:
                break

        if flag is False:
            print('NO')

