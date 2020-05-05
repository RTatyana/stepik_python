
l = [i for i in range(1, 5)]

# 1 вариант
r = []
for i in range(len(l)):
    r.append(l[len(l)-i-1])
print(r)


r2 = list(reversed(l))
print(r2)


print(l[::-1])

# save next
# modify previous
# make previous as head
# move to next node
# if next == NULL then head = next

# head 1 2 3 4 ... tail > null

# for i in range(len(l)):
#     if l[i+1] is None:
#         next = l[i-len(l)+1]
#         node = l[i-len(l)]
#         head = l[i]

# 2 вариант
# prev = null
# next = null
# el = list;
#
# while (el != null) {
#   next = el->next;
#   el->next = prev;
#   prev = el;
#   el = next;
# }

# for (element *cur, *pr = null, *nx = list; (cur = nx) ? (nx = cur->next) : 0; cur->next = pr, pr = cur);


# 3 вариант
# G>reverse( List ) -> reverse( List, [] ).
# G>reverse( [ H | T ], R ) -> reverse( T, [ H | R ] );
# G>reverse( [], R ) -> R.
# G>
#
#
# reverse( List ) -> reverse( List, [] ). %% [] - это пустой список
#
# %% reverse с 2-мя параметрами
#
# %% первый аргумент - непустой список с первым элементом H и хвостом T ->
# %% добавить H ко второму аргументу (это тоже список), повторить с остатком списка T
# reverse( [ H | T ], R ) -> reverse( T, [ H | R ] );
#
# %% первый аргумент - пустой список -> вернуть второй аргумент
# reverse( [], R ) -> R.


el = iter(l)
first = next(el)
a = all(element == first for element in el)
print(a)

