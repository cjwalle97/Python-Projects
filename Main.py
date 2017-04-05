from AStar import astar
from AStar import Node
from AStar import printpath

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