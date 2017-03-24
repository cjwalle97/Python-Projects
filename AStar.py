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
    '''get the neighbors    nodes the list of nodes to check    current the node to check nodes with'''
    # directions
    '''put those in a list'''
    '''loop over that list'''
    '''make a tuple that represents the node as a direction'''
    # example bob = Node("bob", 1, 2)
    #(1,2) != bob
    #(1,2) == (bob.x, bob.y)
    #if we get an equality then add the actual node to the neighbors list
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
    i = 0
    for i in nodes:
        node = (i.x, i.y)
        if node in directions:
            neighbors.append(i)
    return neighbors

def findlowestf(neighbors):
    '''calculate the f_cost of all neighbors'''
    ''''''
    '''return the lowest number amoung them'''

def main():
    '''main'''
    a = Node('a', 0, 0)
    b = Node('b', 1, 0)
    c = Node('c', 1, 1)
    d = Node('d', 0, 1)
    e = Node('e', 2, 0)
    nodes = [a, b, c, d, e]
    neighbors = get_neighbors(a, nodes)
    test0 = [b, c, d]  # tests to see if equality
    testing = True
    if testing:
        # test a
        tests = [test0]
        i = 0
        for test in tests:
            if neighbors == test:
                success = True
                print 'pass', "test ", i
            else:
                success = False
                print 'fail', "test ", i
            i = i + 1

    a.neighbors = neighbors
    for i in a.neighbors:
        print i


if __name__ == '__main__':

    main()