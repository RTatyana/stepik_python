for _ in range(int(input())):
    n = int(input())
    s = input()

    res = 0
    i_odd = 0
    s_new = ''

    for i in s:
        if int(i) % 2 != 0:
            s_new += i
            if len(s_new) == 2:
                break

    if len(s_new) == 2:
        print(s_new)
    else:
        print(-1)

    # for i in range(len(str(s))):
    #     if int(str(s)[i]) % 2 > 0:
    #         i_odd += 1
    #         s_new = s_new + str(s)[i]
    #         if i_odd > 1:
    #             res = s_new
    #             break
    #
    # if i_odd <= 1:
    #     print(-1)
    # else:
    #     print(res)

    #
    # def sum_number(s):
    #     sum_num = 0
    #     for i in range(len(str(s))):
    #         sum_num = sum_num + int(str(s)[i])
    #     return sum_num
    #
    #
    # def del_null(st):
    #     st_new = st
    #     i = 0
    #     while str(st)[i] == '0':
    #         st_new = str(st)[i + 1:]
    #         i += 1
    #     return st_new
    #
    #
    # def del_null_2(s):
    #     st_new = s
    #     # print(int(st_new) % 10)
    #     while (int(st_new) % 10) == 0:
    #         st_new = int(s) // 10
    #     return st_new
    #
    #
    # if s % 2 > 0 and sum_number(s) % 2 == 0:
    #     res = s
    #
    # if sum_number(s) % 2 > 0:
    #     for i in range(len(str(s))):
    #         if str(s)[i] == '1':
    #             s_new = str(s)[:i] + str(s)[i + 1:]
    #             s_new_new = del_null_2(s_new)
    #             if int(s_new_new) % 2 > 0:
    #                 res = s_new_new
    #                 break
    #             else:
    #                 # s_new_new = s_new[:-1]
    #                 # res = s_new_new
    #                 res = 0
    #                 break
    #
    # if sum_number(s) % 2 == 0 and s % 2 == 0:
    #     # s_new = str(s)[:-1]
    #     # res = s_new
    #
    #     for i in range(1, len(str(s)) - 1):
    #         k = -i
    #         if int(str(s)[k]) % 2 > 0:
    #             s_new = str(s)[:k + 1]
    #             res = s_new
    #             break
    #         else:
    #             res = 0
    #
    # if res == 0 or res == '':
    #     print(-1)
    #     # print(sum_number(s))
    #     # print(sum_number(s) % 2)
    #     # print(int(s) % 2)
    # else:
    #     r = del_null(str(res))
    #     print(r)
    #     # print(sum_number(r))
    #     # print(sum_number(r) % 2)
    #     # print(int(r) % 2)
