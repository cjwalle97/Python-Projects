class Node(object):
    def __init__(self, x, y, name):
        self.name = name
        self.parent = None

a = Node(0, 0, 'a')

b = Node(1, 0, 'b')

c = Node(2, 0, 'c')

d = Node(3, 0, 'd')

e = Node(0, 1, 'e')

a.parent = None

b.parent = a

c.parent = b

d.parent = c

e.parent = a

