for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    b = []
    a1 = []
    sub_a = []
    max_a = None

    for i in range(len(a)):
        if a[i] > 0:
            b.append(True)
        else:
            b.append(False)

    for i in range(len(a)):
        if b[i] is True:
            a1.append(a[i])
            if i + 1 == n or b[i + 1] is False:
                max_a = max(a1)
                sub_a.append(max_a)
                a1 = []

        if b[i] is False:
            a1.append(a[i])
            if i + 1 == n or b[i + 1] is True:
                max_a = max(a1)
                sub_a.append(max_a)
                a1 = []

    print(sum(sub_a))
