import re

for _ in range(int(input())):
    n = int(input())
    s = str(input())

    arr = [[[0, 0], 0]]
    arr_2 = []
    x = 0
    y = 0
    a = -1
    b = -1
    k = 0
    i = 0
    diff = 0

    if re.sub('R', '', s) == '' or re.sub("U", "", s) == '' or re.sub(r"D", "", s) == '' or re.sub(r"L", "", s) == '':
        print(-1)
    else:
        for i in range(1, int(len(s)) + 1):
            if str(s[i - 1]) == 'L':
                x = x - 1
                y = y
                i = i
                arr.append([[x, y], i])
            if str(s[i - 1]) == 'R':
                x = x + 1
                y = y
                i = i
                arr.append([[x, y], i])
            if str(s[i - 1]) == 'U':
                x = x
                y = y + 1
                i = i
                arr.append([[x, y], i])
            if str(s[i - 1]) == 'D':
                x = x
                y = y - 1
                i = i
                arr.append([[x, y], i])
            for l in range(0, len(arr) - 1):
                if arr[-1][0] == arr[l][0]:
                    # and i - l - b < diff:
                    a = arr[l][1] + 1
                    b = arr[-1][1]
                    diff = b - a + 1

                    if not arr_2:
                        arr_2.append([[a, b], diff])

                    if arr_2 != [] and diff < int(arr_2[0][1]):
                        arr_2 = []
                        arr_2.append([[a, b], diff])

                    if diff == 2:
                        break

                    for h in range(diff):
                        del arr[l]
                    # arr = []
                    # arr.append([[0, 0], 0])
                    # arr.append([[x, y], i])
                    break
            if diff == 2:
                break

        if a == -1 and b == -1:
            print(-1)
        else:
            print(arr_2[0][0][0], arr_2[0][0][1])
