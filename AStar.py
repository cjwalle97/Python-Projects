class Node(object):
    '''node'''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None
        self.g = None
        self.h = None
        self.f = None

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
    for i in nodes:
        node = (i.x, i.y)
        if node in directions:
            neighbors.append(i)
    return neighbors

def find_g(node, neighbors):
    gcosts = []
    for i in neighbors:
        xdifference = i.x - node.x
        ydifference = i.y - node.y
        totaldifference = xdifference + ydifference
        if totaldifference == 1 or totaldifference == -1:
            i.g = 10
            gcosts.append(i.g)
        else:
            i.g = 14
            gcosts.append(i.g)
    return gcosts

def find_h(neighbors, destination):
    hcosts = []
    for i in neighbors:
        xleft = destination.x - i.x
        if xleft < 1:
            xleft = xleft * -1
        yleft = destination.y - i.y
        if yleft < 1:
            yleft = yleft * -1
        totalleft = xleft + yleft
        i.h = totalleft * 10
        hcosts.append(i.h)
    return hcosts

def find_f(neighbors):
    fcosts = []
    for i in neighbors:
        i.f = i.g + i.h
        fcosts.append(i.f)
    return fcosts

def find_lowest(neighbors):
    lowest = neighbors[0]
    for i in neighbors:
        if i.f < lowest.f:
            lowest = i
    return lowest

def astar(nodes, start, destination):
    path = []
    current = start
    while current != destination:
        path.append(current)
        neighbors = get_neighbors(current, nodes)
        find_g(current, neighbors)
        find_h(neighbors, destination)
        find_f(neighbors)
        next_node = find_lowest(neighbors)
        previous = current
        current = next_node
        current.parent = previous
    if current == destination:
        path.append(destination)
        return path


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

    gtest = find_g(a,neighbors) #tests to see if the findg function works
    for i in gtest:
        print i

    htest = find_h(neighbors, e) #tests to see if the findh function works
    for i in htest:
        print i 

    ftest = find_f(neighbors) #tests to see if the findf function works
    for i in ftest:
        print i
    
    lowtest = find_lowest(neighbors) #tests to see if the findlowestf function works
    print lowtest

    astartest = astar(nodes, a, e) #tests to see if the astar function works
    for i in astartest:
        print i

if __name__ == '__main__':

    main()