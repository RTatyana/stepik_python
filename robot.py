for _ in range(int(input())):
    n = int(input())
    s = str(input())

    res_st = []
    res_ST = []

    if len(s) < 4:
        for i in range(len(s) - 1):
            st = str(s[i]) + str(s[i + 1])
            if st == 'UD' or st == 'DU' or st == 'LR' or st == 'RL':
                res_st = [i + 1, i + 2]
                break

    else:
        for i in range(len(s) - 1):
            st = s[i] + s[i + 1]
            if st == 'UD' or st == 'DU' or st == 'LR' or st == 'RL':
                res_st = [i + 1, i + 2]
                break
        for i in range(len(s) - 3):
            ST = s[i] + s[i + 1] + s[i + 2] + s[i + 3]
            if ST == 'LURD' or ST == 'URDL' or ST == 'RDLU' or ST == 'DLUR':
                res_ST = [i + 1, i + 4]
                break
            if ST == 'ULDR' or ST == 'LDRU' or ST == 'DRUL' or ST == 'RULD':
                res_ST = [i + 1, i + 4]
                break

    if res_st:
        print(res_st[0], res_st[1])
    elif res_ST:
        print(res_ST[0], res_ST[1])
    else:
        print(-1)
