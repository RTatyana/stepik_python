for _ in range(int(input())):
    n = int(input())

    k = 2

    while n % (2 ** k - 1) != 0 and k < n:
            k += 1

    if n % (2 ** k - 1) == 0:
        print(int(n / (2 ** k - 1)))
    else:
        print('Нет решения')
