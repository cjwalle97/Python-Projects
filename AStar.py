class Node(object):
    def __init__(self, x, y, name):
        self.name = name
        self.parent = None

a = Node(0, 0, 'a')

b = Node(1, 0, 'b')

c = Node(2, 0, 'c')

d = Node(3, 0, 'd')

e = Node(0, 1, 'e')

f = Node(0, 2, 'f')

g = Node(0, 3, 'g')

h = Node(-1, 0, 'h')

i = Node(-2, 0, 'i')

j = Node(-3, 0, 'j')

k = Node(0, -1, 'k')

l = Node(0, -2, 'l')

m = Node(0, -3, 'm')

a.parent = None

b.parent = a

c.parent = b

d.parent = c

e.parent = a

f.parent = e

g.parent = f

h.parent = a

i.parent = h

j.parent = i

k.parent = a

l.parent = k

m.parent = l

def retrace(start, destination):
    path = []
    current = start
    while current != destination:
        path.append(current)
        current = current.parent
        if current == destination:
            path.append(destination)
    return path

def printpath(path):
    for i in path:
        print 'Node: ', i.name

printpath(retrace(m,a))