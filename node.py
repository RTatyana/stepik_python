import copy
import random


# Объявление элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Определение первого и последнего элемента списка, его длина. Распечатка и очистка списка
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next != None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    # определение длины списка
    def len(self):
        self.length = 0
        if self.first != None:
            self.length += 1
            current = self.first
            while current.next != None:
                current = current.next
                self.length += 1
        return self.length

    # добавление элемента в начало списка
    def push(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            self.first = Node(x, self.first)

    # добавление элемента в конец списка
    def add(self, x):
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.first = Node(x, None)
            self.last = self.first
        # elif self.last == self.first:
        #     # один элемент в списке
        #     self.last = Node(x, None)
        #     self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    # вставка элемента на определенную позицию
    def insert_nth(self, i, x):
        if (self.first == None):
            self.first = Node(x, self.first)
            self.last = self.first.next
            return
        curr = self.first
        count = 0
        if i == 0 or i == 1:
            self.first = Node(x, self.first)
            return
        else:
            while curr != None:
                count = count + 1
                if count == i - 1:
                    curr.next = Node(x, curr.next)
                    if curr.next.next == None:
                        self.last = curr.next
                    break
                curr = curr.next

    # удаление головного элемента
    def pop(self):
        oldhead = self.first
        if oldhead == None:
            return None
        self.first = oldhead.next
        if self.first == None:
            self.last = None
        return oldhead.value

    # удаление элемента из списка
    def Del(self, i):
        if (self.first == None):
            return
        old = curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == self.last:
                    self.last = curr
                    break
                else:
                    old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    # вставка элкмента в отсортированный список

    def sorted_insert(self, x):
        if (self.first == None):
            self.first = Node(x, self.last)
            return
        if self.first.value > x:
            self.first = Node(x, self.first)
            return
        old = curr = self.first
        while curr != None:
            if curr.value > x:
                curr = Node(x, curr)
                old.next = curr
                return
            old = curr
            curr = curr.next
        curr = Node(x, None)
        old.next = curr

    # удаление повторяющихся элементов
    def remove_duplicates(self):
        if (self.first == None):
            return
        old = curr = self.first
        while curr != None:
            _del = 0
            if curr.next != None:
                if curr.value == curr.next.value:
                    curr.next = curr.next.next
                    _del = 1
            if _del == 0:
                curr = curr.next


L = LinkedList()

L.add(1)
L.add(2)
L.add(3)
L.insert_nth(3, 66)
L.push(5)
L.pop()
L.Del(3)
L.sorted_insert(56)
L.sorted_insert(56)
L.remove_duplicates()

# копирование списка
L2 = copy.deepcopy(L)

print(L)
print(L.len())
print(L2)
