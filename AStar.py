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

def find_g(node, neighbor):
    xdifference = neighbor.x - node.x
    ydifference = neighbor.y - node.y
    totaldifference = xdifference + ydifference
    if totaldifference == 1 or totaldifference == -1:
        gcost = 10
    else:
        gcost = 14
    neighbor.g = gcost
    return gcost

def find_h(node, goal):
    xleft = goal.x - node.x
    if xleft < 1:
        xleft = xleft * -1
    yleft = goal.y - node.y
    if yleft < 1:
        yleft = yleft * -1
    totalleft = xleft + yleft
    hcost = totalleft * 10
    return hcost

def astar(graph, start, goal):
    path = []
    current = start
    _start = start
    openlist = []
    closedlist = []
    openlist.append(_start)
    while open:
        current = openlist[0]
        closedlist.append(current)
        openlist.remove(current)
        get_neighbors(current, graph)
        for neighbor in current.neighbors:
            tentative_g = current.g + find_g(current, neighbor)
            if neighbor not in openlist:
                openlist.append(neighbor) 
            if tentative_g >= neighbor.g:
                continue
        neighbor.g = find_g(current, neighbor) + current.g
        neighbor.h = find_h(neighbor, goal)
        neighbor.f = neighbor.g + neighbor.h
    return path


def main():
    '''main'''
    graph = []
    index = 0
    for y in range(10):
        for x in range(10):
            name = str(index)
            node = Node(name, x, y)
            graph.append(node)
            index += 1


if __name__ == '__main__':

    main()