from graph import get_neighbors
from graph import Graph
from graph import Node
from drawablenode import DrawableNode

Grid = Graph(5)

def retrace(start, destination):
    path = []
    current = start
    while current != destination:
        path.append(current)
        current = current.parent
        if current == destination:
            path.append(destination)
    return path

def astar(start, destination):
    Children = []
    previous = None
    target = None
    current = start
    while current != destination:
        neighbors = get_neighbors(current, Grid)
        for i in neighbors:
            if 
                '''Should make the value of G = 10'''
            if 
                '''Should make the value of G = 14'''

            '''finds the value of H'''

            '''Adds G and H to make F then finds the lowest F cost'''
                
                '''Moves Current to the node with the lowest F cost'''
                previous = current
                current = target
                current.parent = previous
        
