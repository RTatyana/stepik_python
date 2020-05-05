for _ in range(int(input())):
    n = int(input())
    arr = [int(a) for a in input().split()]

    count = 0


    def sum_arr(arr):
        sum = 0
        for i in range(len(arr)):
            sum = sum + arr[i]
        return sum


    def multi_arr(arr):
        multi = 0
        for i in range(len(arr)):
            multi = multi * arr[i]
        return multi


    if sum_arr(arr) != 0 and multi_arr(arr) != 0:
        count = 0

    if multi_arr(arr) == 0:
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] += 1
                count += 1

    if sum_arr(arr) == 0:
        for i in range(len(arr)):
            arr[i] += 1
            count += 1
            if arr[i] != 0:
                break
            else:
                count -= 1
                arr[i] -= 1

    print(count)
