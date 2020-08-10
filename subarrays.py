for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    b = sorted(set(a))

    if k < len(b):
        print(-1)
    else:
        l = 0
        while (l + k) <= len(a):
            c = a[l:l + k]

            while sum(b) != sum(c):
                for i in range(len(b)):
                    if b[i] not in a[l:l + k] and l == 0:
                        a.insert(1, b[i])
                    if b[i] not in a[l:l + k]:
                        a.insert(l + k - 1, b[i])
                    c = a[l:l + k]
                    # if (sum(b) - sum(c)) % b[i] == 0:
                    #     a.insert(l + 1, b[i])
            l = l + 1

        print(len(a))
        print(*a)

    # if k > len(b):


                # if k > 2:
                #
                #     for i in range(len(c) - 1):
                #         if c[i] == c[i + 1]:
                #             for j in range(len(b)):
                #                 if b[j] != c[i]:
                #                     a.insert(i + 1, b[j])


