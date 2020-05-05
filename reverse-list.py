import random


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.curr = None
        self.first = None
        self.last = None
        self.old = None
        self.len = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList = ' + str(current.value) + ' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
                return out + ''
            return ''


def main():
    L = LinkedList()
    for i in range(0, 2000):
        _r = int(random.uniform(0, 100))
        L.old = L.curr = L.first
        L.len = 0
        while L.curr != None:
            L.old = L.curr
            L.curr = L.curr.next
        if L.len == 0:
            L.curr = Node(_r, None)
            L.old.next = L.curr
    print(L)


main()
