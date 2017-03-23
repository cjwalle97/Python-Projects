from graph import Graph

grid = Graph(3)

class Node(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None
        f = None
        g = None
        h = None


a = Node('a', 0, 0)

b = Node('b', 1, 0)

c = Node('c', 1, 1)

d = Node('d', 0, 1)

e = Node('e', 2, 0)

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

def get_neighbors(current, destination):
    right = Node('right', current.x + 1, current.y)
    top_right = Node('top_right', current.x + 1, current.y + 1)
    top = Node('top', current.x, current.y + 1)
    top_left = Node('top_left', current.x - 1, current.y + 1)
    left = Node('left', current.x - 1, current.y)
    bottom_left = Node('bottom_left', current.x - 1, current.y - 1)
    bottom = Node('bottom', current.x, current.y - 1)
    bottom_right = Node('bottom_right', current.x + 1, current.y - 1)
    neighbors = [right, top_right, top, top_left, left, bottom_left, bottom, bottom_right]
    lowest = neighbors[0]
    for i in neighbors:
        currenttemp = (i.x - current.x) + (i.y - current.y)
        if currenttemp == 1 or -1:
            i.g = 10
        else:
            i.g = 14
        desttemp = (destination.x - i.x) + (destination.y - current.y)
        i.h = desttemp
        i.f = i.g + i.h
        if i.f < lowest.f:
            lowest = i
    return lowest

def astar(start, destination):
    current = start
    target = None
    previous = None
    while current != destination:
        target = get_neighbors(current, destination)
        previous = current
        current = target
        current.parent = previous
    return destination


astar(a, e)

