class Node(object):
    '''node'''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None
        self.f = None
        self.g = None
        self.h = None

    def __str__(self):
        '''overload string for print'''
        return "Name: " + self.name + "\nPosition: " + str(self.x) + ", " + str(self.y)


def retrace(start, destination):
    '''retrace the path'''
    path = []
    current = start
    while current != destination:
        path.append(current)
        current = current.parent
        if current == destination:
            path.append(destination)
    return path

def printpath(path):
    '''print the path'''
    for i in path:
        print 'Node: ', i.name

def get_neighbors(current, nodes):
    right = (current.x + 1, current.y)
    top_right = (current.x + 1, current.y + 1)
    top = (current.x, current.y + 1)
    top_left = (current.x - 1, current.y + 1)
    left = (current.x - 1, current.y)
    bottom_left = (current.x - 1, current.y - 1)
    bottom = (current.x, current.y - 1)
    bottom_right = (current.x + 1, current.y - 1)
    directions = [right, top_right, top, top_left, left, bottom_left, bottom, bottom_right]
    neighbors = []
    for i in nodes:    
        node = (i.x, i.y)
        if node in directions:
            neighbors.append(i)

def main():
    '''main'''
    a = Node('a', 0, 0)
    b = Node('b', 1, 0)
    c = Node('c', 1, 1)
    d = Node('d', 0, 1)
    e = Node('e', 2, 0)
    nodes = [a, b, c, d, e]
    neighbors = get_neighbors(a, nodes)
    test0 = [b, c, d] #tests to see if equality
    tests = [test0]
    i = 0
    for test in tests:
        if neighbors == test:
            success = True
            print 'pass', "test ", i
        else:
            success = Falseprint 'fail', "test ", i
        i = i + 1

    if __name__ == '__main__':

        main()