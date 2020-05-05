answer_print = []

for T in range(int(input())):
    S = str(input())
    S_new = ''

    for i in range(len(S)):
        if int(S[i]) == 0:
            S_new = S_new + str(S[i])
            l = 0
            r = 0

        if int(S[i]) >= 1:
            l = 0
            r = 0
            for j in range(len(S_new)):
                if S_new[j] == '(':
                    l += 1
                if S_new[j] == ')':
                    r += 1

            if l == r == 0 or int(S[i - 1]) == 0:
                for k in range(int(S[i])):
                    S_new = S_new + '('
                S_new = S_new + S[i]
                for k in range(int(S[i])):
                    S_new = S_new + ')'

            if l == r and l >= 1 and S[i] == S[i - 1]:
                for k in range(int(S[i])):
                    S_new = S_new[: - 1]
                S_new = S_new + S[i]
                for k in range(int(S[i])):
                    S_new = S_new + ')'

            if l == r and l >= 1 and S[i] < S[i - 1]:
                S_new = S_new[: - int(S[i])] + S[i]
                for k in range(int(S[i])):
                    S_new = S_new + ')'

            if l == r and l >= 1 and S[i] > S[i - 1] and int(S[i - 1]) != 0:
                S_new = S_new[: - int(S[i - 1])]
                for k in range(int(S[i]) - int(S[i - 1])):
                    S_new = S_new + '('
                S_new = S_new + S[i]
                for k in range(int(S[i])):
                    S_new = S_new + ')'

    # print(S_new)

    row_print = 'Case #' + str(T + 1) + ': ' + str(S_new)
    answer_print.append(row_print)

for row_print in answer_print:
    print(row_print)
