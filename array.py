for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]

    count_even = 0
    count_odd = 0
    flag = False

    if n % 2 == 0:
        for a in arr:
            if a % 2 == 0:
                count_even += 1
            if a % 2 > 0:
                count_odd += 1
            if count_odd != 0 and count_even != 0:
                flag = True
                break

    else:
        for a in arr:
            if a % 2 > 0:
                count_odd += 1
                break
        if count_odd != 0:
            flag = True

    if flag is True:
        print('YES')
    else:
        print('NO')
