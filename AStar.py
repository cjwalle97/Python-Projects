class Node(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = List(parents)

a = Node('a', 0, 0)

b = Node('b', 1, 0)

c = Node('c', 2, 0)

d = Node('d', 3, 0)

e = Node('e', 0, 1)

f = Node('f', 0, 2)

g = Node('g', 0, 3)

h = Node('h', -1, 0)

i = Node('i', -2, 0)

j = Node('j', -3, 0)

k = Node('k', 0, -1)

l = Node('l', 0, -2)

m = Node('m', 0, -3)

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

def neighborcheck(node):
    '''checks all sides of a Node in order to determine if there is another Node nearby. Nearby nodes become Parents'''
    rightcheck =    Node('right', node.x + 1, node.y)
    bottomright = Node('botright', node.x + 1, node.y - 1)
    bottom = Node('bottom', node.x, node.y - 1)
    bottomleft = Node('botleft', node.x - 1, node.y - 1)
    left = Node('left', node.x - 1, node.y)
    topleft = Node('topleft', node.x - 1, node.y + 1)
    top = Node('top', node.x, node + 1)
    topright = Node('topright', node.x + 1, node.y + 1)
    if 

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
