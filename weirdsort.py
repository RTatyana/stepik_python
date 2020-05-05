for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    p = [int(j) for j in input().split()]

    k = len(a)
    max_a = a[0]
    num = 1
    flag = False
    l = []
    b = a.sort()

    while a != a.sort():

        for i in range(k):
            if a[i] >= max_a:
                max_a = a[i]
                num = i + 1

            for j in range(len(p)):
                if (num - 1) != (len(a) - 1) and (num in p):
                    l.append(a[num - 1])
                    a[num - 1] = a[num]
                    a[num] = l[0]
                    print(a)
                    l = []
                    flag = True
                    break
                elif a == b:
                    flag = True
                    break
                else:
                    flag = False
                    break


        # k = k - 1

    if flag is True:
        print('YES')
    else:
        print('NO')
