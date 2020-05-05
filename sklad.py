for _ in range(int(input())):
    n = int(input())

    arr = []

    for i in range(n):
        x, y = map(int, (input().split()))
        arr.append([x, y])

    arr.sort()
    # print(arr)

    path = ''

    for x in range(arr[0][0]):
        path = path + 'R'
    for y in range(arr[0][1]):
        path = path + 'U'

    for i in range(n - 1):
        if arr[i][1] > arr[i + 1][1]:
            print('NO')
            path = ''
            break
        else:
            delta_x = arr[i + 1][0] - arr[i][0]
            delta_y = arr[i + 1][1] - arr[i][1]

            for x in range(delta_x):
                path = path + 'R'
            for y in range(delta_y):
                path = path + 'U'

    if path != '':
        print('YES')
        print(path)
