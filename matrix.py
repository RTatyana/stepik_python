import numpy

answer_print = []

for T in range(int(input())):
    N = int(input())

    r = 0
    c = 0
    trace = 0
    matrix = []
    row = []
    for i in range(N):
        row = [int(j) for j in input().split()]
        matrix.append(row)

    for i in range(N):
        trace += matrix[i][i]

    for i in range(N):
        row = sorted(matrix[i])
        for j in range(N - 1):
            if row[j] == row[j + 1]:
                r += 1
                break

    for j in range(N):
        matrix = numpy.array(matrix)
        column = sorted(matrix[:, j])
        for n in range(1, N):
            if column[n - 1] == column[n]:
                c += 1
                break

    row_print = 'Case #' + str(T + 1) + ': ' + str(trace) + ' ' + str(r) + ' ' + str(c)
    answer_print.append(row_print)

for row_print in answer_print:
    print(row_print)
