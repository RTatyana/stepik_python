for _ in range(int(input())):

    n, x = map(int, input().split())
    s = input()

    count_p = 0

    def calc_x(s):
        x0 = 0
        x1 = 0
        for j in range(len(s)):
            if s[j] == '0':
                x0 += 1
            else:
                x1 += 1

        x = x0 - x1
        return x

    xs = calc_x(s)
    # print(xs)

    if n < len(str(x)) or xs < 0:
        print(0)
    if xs > 0 and x % xs == 0:
        count_p += 1
        t = ''
        for k in range(int(x // xs) - 1):
            t = t + s
        for l in range(len(s)):
            t = t + s[l]
            if calc_x(t) == x:
                count_p += 1

        t = t + s
        for l in range(len(s)):
            t = t + s[l]
            if calc_x(t) == x:
                count_p += 1

        print(count_p)
    if xs > 0 and x % xs != 0:
        for l in range(len(s)):
            s0 = ''
            s0 = s0 + s[l]
            if calc_x(s0) == x:
                count_p += 1
        print(count_p)
    if xs == 0:
        print(-1)
