import math

for _ in range(int(input())):
    n = int(input())

    flag = False

    if n < 24:
        print('NO')
    elif n == 24:
        print('YES')
        print(2, 3, 4)
    else:

        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                a = i
                n = n / i

                for j in range(a + 1, int(math.sqrt(n))):
                    if n % j == 0:
                        b = j
                        c = int(n / j)

                        if c != b and a != c:
                            print('YES')
                            print(a, b, c)
                            flag = True
                            break
            if flag is True:
                break

        if flag is False:
            print('NO')