for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]


    def find_min(arr):
        min_el = max(arr)
        for i in range(len(arr)):
            if arr[i] != -1 and arr[i] < min_el:
                min_el = arr[i]
        return min_el


    def find_max(arr):
        max_el = min(arr)
        for i in range(len(arr)):
            if arr[i] != -1 and arr[i] > max_el:
                max_el = arr[i]
        return max_el


    def max_m(arr):
        maximal_m = abs(arr[1] - arr[0])
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) > maximal_m:
                maximal_m = abs(arr[i + 1] - arr[i])
        return maximal_m


    min_el = find_min(arr)
    max_el = find_max(arr)
    max_diff = 0

    if min_el == -1 or max_el == -1:
        print(max_diff, 0)
    elif max_el == min_el and max_el != -1:
        print(max_diff, max_el)
    else:
        for j in range(min_el, max_el):
            arr_new = []
            for i in range(len(arr)):
                if arr[i] == -1:
                    arr_new.append(min_el)
                else:
                    arr_new.append(arr[i])
            maximal_m = max_m(arr_new)
            if max_diff == 0:
                max_diff = maximal_m
            elif maximal_m < max_diff:
                max_diff = maximal_m
            else:
                k = min(min_el, (max_el - max_diff))
                break
            k = min_el
            min_el = min_el + 1

        print(max_diff, k)
