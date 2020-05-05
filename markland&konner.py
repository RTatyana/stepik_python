for _ in range(int(input())):
    # arr = [int(i) for i in input().split()]
    # n = arr[0]
    # s = arr[1]
    # k = arr[2]

    n, s, k = map(int, input().split())

    # A = [int(j) for j in input().split()]

    A = list(map(int, input().split()))

    x = 0

    for x in range(n):
        if ((s + x) not in A and (s + x) <= n) or ((s - x) not in A and (s - x) > 0):
            break

    print(x)
