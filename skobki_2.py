for _ in range(int(input())):
    n = int(input())

    a = []


    def recursive_def_1(n):
        if n == 2:
            s = '()'
            a.append(s)
            return s
        else:
            s = '(' + str(recursive_def_1(n - 2)) + ')'
            if s not in a:
                a.append(s)
                return s


    def recursive_def_2(n):
        if n == 2:
            s = '()'
            if s not in a:
                a.append(s)
            return s
        else:
            s = '()' + str(recursive_def_2(n - 2))
            s1 = str(recursive_def_2(n - 2)) + '()'
            if s not in a:
                a.append(s)
                return s
            if s1 not in a:
                a.append(s1)
                return s1


    def recursive_def_3(a, n):
        for i in a:
            s = '()' + i
            if s not in a and len(str(s)) == n:
                a.append(s)
            s1 = i + '()'
            if s1 not in a and len(str(s1)) == n:
                a.append(s1)


    if n % 2 != 0:
        print('NO')
    else:
        recursive_def_1(n)
        recursive_def_2(n)
        recursive_def_3(a, n)
        for i in range(len(a)):
            if len(str(a[i])) == n:
                print(a[i])
