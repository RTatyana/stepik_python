for i in range(int(input())):
    n = int(input())
    A = [int(j) for j in input().split()]

    X = sum(A)

    Y1 = 0
    Y2 = 0
    result = 'YES'
    for j in range(n - 1):
        Y1 += A[j]
        Y2 += A[-(j+1)]
        if Y1 >= X:
            result = 'NO'
        if Y2 >= X:
            result = 'NO'
    print(result)

