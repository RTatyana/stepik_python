n = int(input())

a = []


def recursive_def(a, n):
    a0 = ''
    a1 = ''
    for i in range(int(n / 2 - 1)):
        a0 = a0 + '('
    for i in range(int(n / 2 - 1)):
        a0 = a0 + ')'

    for i in range(n - 1):
        a1 = a1 + '()'

    if n == 2:
        return a
    else:
        a.append(a0)
        a.append(a1)
        for i in range(1, len(a)):
            a3 = '()' + str(a[i])
            a4 = str(a[i]) + '()'
            a.append(a3)
            a.append(a4)
        recursive_def(a, n - 2)
        return a


if n % 2 != 0:
    print(a)
elif n == 2:
    a.append('()')
    print(a)
else:
    recursive_def(a, n)
    # a0 = ''
    # for i in range(int(n / 2)):
    #     a0 = a0 + '('
    # for i in range(int(n / 2)):
    #     a0 = a0 + ')'
    # a.append(a0)
    print(set(a[(n - 1):]))
