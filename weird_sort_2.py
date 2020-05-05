for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    p = [int(j) for j in input().split()]
    l = []
    flag = True
    q = 0

    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if a[j] < a[smallest]:
                smallest = j
                q = 1

        if q == 1 and ((smallest + 1) in p):
            x = a[i]
            a[i] = a[smallest]
            a[smallest] = x
            flag = True
        elif q == 1 and (smallest not in p or (smallest - 1) not in p):
            flag = False
            break
        q = 0

        print(a)

    if flag is True:
        print('YES')
    else:
        print('NO')
