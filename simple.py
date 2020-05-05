for _ in range(int(input())):
    n = int(input())
    s = int(input())

    res = 0
    s_new = ''


    def sum_number(s):
        sum_num = 0
        for i in range(len(str(s))):
            sum_num = sum_num + int(str(s)[i])
        return sum_num


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
        s_new = s
        while (int(str(s_new)[-1]) % 2) == 0 and int(s_new) != 0:
            s_new = int(s_new // 10)
    else:
        s_new = s

    if sum_number(s_new) % 2 == 0:
        res = s_new
    if sum_number(s_new) % 2 > 0:
        for i in range(len(str(s_new))):
            if int(str(s_new)[i]) % 2 > 0:
                s_new_new = str(s_new)[:i] + str(s_new)[i + 1:]
                res = s_new_new
                break
            else:
                res = 0

    if res == 0 or res == '':
        print(-1)
    else:
        r = del_null(str(res))
        print(r)