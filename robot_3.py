for _ in range(int(input())):
    n = int(input())
    s = str(input())

    arr = [[0, 0, 0]]
    x = 0
    y = 0
    l = - 1
    r = n

    for i in range(int(len(s))):
        if str(s[i]) == 'L':
            x -= 1
        elif str(s[i]) == 'R':
            x += 1
        elif str(s[i]) == 'U':
            y += 1
        else:
            y -= 1
        arr.append([x, y, i + 1])
        arr.sort()
    m = len(s) + 1
    for i in range(int(len(s))):
        if arr[i][0] == arr[i + 1][0] and arr[i][1] == arr[i + 1][1]:
            if arr[i + 1][1] - arr[i][2] < m:
                l = arr[i][2] + 1
                r = arr[i + 1][2]
                m = r - l - 1

    if m == len(s) + 1:
        print(-1)
    else:
        print(l, r)
