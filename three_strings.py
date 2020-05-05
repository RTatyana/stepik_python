for _ in range(int(input())):
    a = str(input())
    b = str(input())
    c = str(input())

    flag = True

    for i in range(len(c)):
        if c[i] == a[i]:
            b = b[:i] + c[i] + b[(i + 1):]
        if c[i] == b[i]:
            a = a[:i] + c[i] + a[(i + 1):]
        else:
            flag = False
            break

    if flag is True:
        print('YES')
    else:
        print('NO')
