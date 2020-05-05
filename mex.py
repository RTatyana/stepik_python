q, x = map(int, input().split())
a = []
mex = 0
mex_1 = 0

for i in range(q):
    y = int(input())

    a.append(y)

    if a[0] != 0:
        mex = 0

    elif a[0] == 0 and len(a) == 1:
        mex = 1

    #  1. проверяем надо ли вообще что-то делать: если отсортированный массив без "дырок", то  мех = макс + 1
    else:
        a.sort()
        for j in range(1, len(a)):
            if a[j] == a[j - 1] + 1 or a[j] == a[j - 1]:
                if a[j] == 0:
                    a[j] = a[j] + x
                    mex = max(a) + 1
                else:
                    mex = max(a) + 1
            else:
                A = a[j - 1] + 1  # пропущенное в отсортированном массиве число

                # 2. если дырки есть (обозначаем первую A), то смотрим на что делится х без остатка(это будет b):
                #  на 2 - если последнее число делится на 2

                list_num = [int(k) for k in map(int, str(x))]
                if (list_num[-1]) % 2 == 0:
                    b = 2
                    n = x / b

                    # 3. дальше а массиве найдем такое ближайшее число, которое N = A - x/a (или N = A - n)
                    for m in range(len(a)):
                        if a[m] == A - n:
                            a.append(A)
                        else:
                            mex = A

                #  на 3 - если сумма чисел делится на 3
                list_num = [int(k) for k in map(int, str(x))]
                summa = sum(list_num)
                summa_2 = int(summa / 3)
                if sum(list_num) % 3 == 0:
                    b = 3
                    n = x / b

                    for m in range(len(a)):
                        if a[m] == A - n:
                            a[m] = A
                            break
                        else:
                            mex = A

                # на 5 - если последнее число - 0 или 5
                if list_num[-1] == 0 or list_num[-1] == 5:
                    b = 5
                    n = x / b


                # if
                #  на 7 - если знакочередующаяся сумма трёхзначных граней* числа a делится на 7, те 1 234 569 делится на 7
                #  тк 1 -234 + 569 делится на 7

                else:
                    mex = A

    if mex_1 == 0:
        print(mex)
    else:
        print(mex_1)

#     elif len(a) > 1:
#         flag = False
#         # b = list(set(a))
#         # b.sort()
#         a.sort()
#         for j in range(0, len(a)):
#
#             if a[j] == a[j - 1] + 1:
#                 flag = True
#             else:
#                 flag = False
#
#             if flag is True:
#                 mex = a[-1] + 1
#
#         a.sort()
#         for k in range(1, i + 1):
#             if a[k] == 0:
#                 a[k] = a[k] + x
#                 a.sort()
#             if a[k] == a[k - 1]:
#                 a[k] = a[k] + x
#                 a.sort()
#                 if a[k] == a[k - 1]:
#                     a[k] = a[k] + x
#                     a.sort()
#             if a[k] - a[k - 1] > 1:
#                 for m in range(i + 1):
#                     if a[k] - 1 == a[m] - x:
#                         a[m] = a[m] - x
#                         a.sort()
#                         # одной итерации прибавления х может быть недостаточно
#                     if a[k] - 1 == a[m] + x:
#                         a[m] = a[m] + x
#                         a.sort()
#                     else:
#                         mex_1 = a[k] - 1
#
#             else:
#                 if mex == 0:
#                     mex = a[-1] + 1
#             # a.sort()
#     if mex_1 == 0:
#         print(mex)
#     else:
#         print(mex_1)
# #
#  1 проверяем надо ли вообще что-то делать: если отсортированный массив без "дырок", то  мех = макс + 1

# 2 если дырки есть (обозначаем первую A), то смотрим на что делится х без остатка(это будет a - ):
#  на 2 - если последнее число делится на 2
#  на 3 - если сумма чисел делится на 3
#  на 5 - если последнее число - 0 или 5
#  на 7 - если знакочередующаяся сумма трёхзначных граней* числа a делится на 7, те 1 234 569 делится на 7
#  тк 1 -234 + 569 делится на 7

#  остальные числа получаем как  n * a = x, т.е надо найти это n
#
# 3 дальше а массиве найдем такое ближайшее число, которое N = A - x/a (или N = A - n)
# если нашли, то делаем arr.append(N), arr.sort() и идем еще раз на п1
# если не нашли - то  mex = А
