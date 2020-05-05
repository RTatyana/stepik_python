for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]


    # def find_min(arr):
    #     min_el = max(arr)
    #     for i in range(len(arr)):
    #         if arr[i] != -1 and arr[i] < min_el:
    #             min_el = arr[i]
    #     return min_el
    #
    #
    # def find_max(arr):
    #     max_el = min(arr)
    #     for i in range(len(arr)):
    #         if arr[i] != -1 and arr[i] > max_el:
    #             max_el = arr[i]
    #     return max_el

    def max_m(arr):
        maximal_m = abs(arr[1] - arr[0])
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) > maximal_m:
                maximal_m = abs(arr[i + 1] - arr[i])
        return maximal_m


    arr_min_1 = []

    if arr[0] != -1 and arr[1] == -1:
        arr_min_1.append(arr[0])

    for i in range(1, len(arr) - 1):
        if arr[i] != -1 and (arr[i + 1] == -1 or arr[i - 1] == -1):
            arr_min_1.append(arr[i])

    if arr[-1] != -1 and arr[n - 1] == -1:
        arr_min_1.append(arr[-1])

    k = (max(arr_min_1) + min(arr_min_1)) / 2

    arr_new = []
    for i in range(len(arr)):
        if arr[i] == -1:
            arr_new.append(k)
        else:
            arr_new.append(arr[i])

    m = max_m(arr_new)

    print(int(m), int(k))
