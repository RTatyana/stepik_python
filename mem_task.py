for _ in range(int(input())):
    arr = [int(j) for j in input().split()]
    A = arr[0]
    B = arr[1]
    count = 0
    i = 9

    while i <= B:
        count = count + 1
        i = i*10 + 9

    print(A*count)



