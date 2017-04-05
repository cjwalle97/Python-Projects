class Node(object):
    '''node'''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
    def __str__(self):
        '''overload string for print'''
        return "Name: " + self.name + "\nPosition: " + str(self.x) + ", " + str(self.y)


def retrace(start, goal):
    '''retrace the path'''
    path = []
    current = goal
    while current.parent is not None:
        path.append(current)
        current = current.parent
    if current.parent is None:
        path.append(current)
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
    gcost = 0
    if neighbor.x == node.x or neighbor.y == node.y:
        gcost = 10
    else:
        gcost = 14
    return gcost

def find_h(node, goal):
    return 10 * (abs(node.x - goal.x) + abs(node.y - goal.y))

def astar(graph, start, goal):
    path = []
    current = start
    openlist = []
    closedlist = []
    openlist.append(current)
    while  goal not in closedlist:
        closedlist.append(current)
        openlist.remove(current)
        tester = get_neighbors(current, graph)
        for neighbor in tester:
            tentative_g = current.g + find_g(current, neighbor)
            if neighbor in closedlist:
                    continue
            if neighbor not in openlist:
                neighbor.g = find_g(current, neighbor) + current.g
                neighbor.parent = current
                openlist.append(neighbor)
            else:
                if tentative_g >= neighbor.g:
                    continue
                else:
                    neighbor.g = tentative_g + current.g
                    neighbor.parent = current
            neighbor.h = find_h(neighbor, goal)
            neighbor.f = neighbor.g + neighbor.h
        openlist.sort(key=lambda node: node.f)
        current = openlist[0]
        if current == goal:
            path = retrace(start, goal)
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
    test = astar(graph, graph[4], graph[25]) 
    printpath(test)   

if __name__ == '__main__':

    main()