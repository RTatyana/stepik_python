answer_print = []

for T in range(int(input())):
    N = int(input())
    row = []
    a = []
    for i in range(N):
        row = [int(j) for j in input().split()]
        a.append(row)
    S = ''

    j = []
    c = []

    flag = False

    for i in range(len(a)):
        if len(j) == 0:
            j.append(a[i])
            flag = True
            S = S + 'J'
        else:
            for k in range(len(j)):
                if a[i][1] <= j[k][0] or a[i][0] >= j[k][1]:
                    flag = True
                else:
                    flag = False
                    break

            if flag is True:
                j.append(a[i])
                S = S + 'J'

            else:
                if len(c) == 0:
                    c.append(a[i])
                    flag = True
                    S = S + 'C'
                else:
                    for m in range(len(c)):
                        if a[i][1] <= c[m][0] or a[i][0] >= c[m][1]:
                            flag = True
                        else:
                            flag = False
                            break

                    if flag is True:
                        c.append(a[i])
                        S = S + 'C'

                    else:
                        S = 'IMPOSSIBLE'
                        break

        if flag is False:
            S = 'IMPOSSIBLE'
            break

    row_print = 'Case #' + str(T + 1) + ': ' + str(S)
    answer_print.append(row_print)

for row_print in answer_print:
    print(row_print)

# 1
# 10
# 1200 1300
# 1210 1345
# 1390 1400
# 5 7
# 6 8
# 3 10
# 345 678
# 124 378
# 111 234
# 18 19
# 678 1190


# 1
# 13
# 360 480
# 420 540
# 600 660
# 0 1440
# 1 3
# 2 4
# 99 150
# 1 100
# 100 301
# 2 5
# 150 250
# 0 720
# 720 1440

# 1
# 5
# 1 2
# 3 24
# 2 6
# 555 788
# 4 5

# 1
# 10
# 0 120
# 120 230
# 231 345
# 346 781
# 780 876
# 877 903
# 905 1080
# 1200 1400
# 1400 1440
# 1 5


#
#
# 4
# 3
# 360 480
# 420 540
# 600 660
# 3
# 1 3
# 2 4
# 0 1440
# 5
# 99 150
# 1 100
# 100 301
# 2 5
# 150 250
# 2
# 0 720
# 720 1440
