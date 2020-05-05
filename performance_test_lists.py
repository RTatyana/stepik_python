import profile
import random
import time


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.old = None
        self.curr = None
        self.ins = 0

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
    t1 = time.time()
    L = LinkedList()

    for i in range(0, 2000):
        _r = int(random.uniform(0, 100))
        if L.first == None:
            L.first = Node(i, None)
        elif L.first.value > _r:
            L.first = Node(_r, L.first)
        else:
            L.old = L.curr = L.first
            L.ins = 0
            while L.curr != None:
                if L.curr.value > _r:
                    L.curr = Node(_r, L.curr)
                    L.old.next = L.curr
                    L.ins = 1
                    break
                L.old = L.curr
                L.curr = L.curr.next
            if L.ins == 0:
                L.curr = Node(_r, None)
                L.old.next = L.curr

    print(L)
    t2 = time.time()
    print("\t%.1f" % ((t2 - t1)))

profile.run('main()')
