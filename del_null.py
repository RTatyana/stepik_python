for _ in range(int(input())):
    st = str(input())

    arr = []
    count = 0
    c_null = 0
    for i in range(len(st)):
        arr.append([int(st[i]), i])

    for i in range(len(arr)):
        if arr[i][0] == 0:
            arr[i][1] = 0
            c_null += 1

    arr.sort()

    for i in range(c_null, len(arr) - 1):
        count = count + (arr[i + 1][1] - arr[i][1] - 1)

    print(count)
