for _ in range(int(input())):
    n = int(input())
    s = int(input())

    res = 0
    s_new = s
    sum_num = 0

    def del_null(st):
        st_new = st
        i = 0
        while str(st)[i] == '0':
            st_new = str(st)[i + 1:]
            i += 1
        return st_new


    if s == 0:
        res = 0

    if s % 2 == 0 and s != 0:
        # for i in range(0, len(str(s_new))):
        #     if (int(str(s_new)[-1]) % 2) == 0 and int(s_new) != 0:
        #         s_new = int(s_new // 10)
        while (int(str(s_new)[-1]) % 2) == 0 and int(s_new) != 0:
            s_new = int(s_new // 10)

    for i in range(len(str(s_new))):
        sum_num = sum_num + int(str(s_new)[i])

    if sum_num % 2 == 0:
        res = s_new
    if sum_num % 2 > 0:
        for i in range(len(str(s_new))):
            if int(str(s_new)[i]) % 2 > 0:
                s_new_new = str(s_new)[:i] + str(s_new)[i + 1:]

                if int(s_new_new) % 2 != 0:
                    res = s_new_new
                else:
                    res = 0
                break
            else:
                res = 0

    if res == 0 or res == '':
        print(-1)
    else:
        r = del_null(str(res))
        print(r)
