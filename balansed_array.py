for _ in range(int(input())):
    n = int(input())

    a = []
    last = None
    s = ''

    if n % 4 != 0:
        print('NO')
    else:
        print('YES')
        a.append(2)
        sum1 = 2
        for i in range(1, int(n / 2)):
            a.append(int(a[i - 1] + 2))
        sum1 = sum(a)
        a.append(1)
        sum2 = 1
        for i in range(int(n / 2) + 1, int(n - 1)):
            a.append(a[i - 1] + 2)
        sum2 = sum(a)
        last = int(2*sum1 - sum2)
        a.append(last)

        # for i in range(len(a)):
        #     s = s + ' ' + str(a[i])
        print(*a)
