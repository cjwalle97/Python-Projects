from graph import get_neighbors
from graph import Graph
from graph import Node
from drawablenode import DrawableNode

Grid = Graph(5)

def astar(start, destination):
    Children = []
    previous = None
    target = None
    current = start
    while current != start:
        neighbors = get_neighbors(current, Grid)
        for i in neighbors:
            if top or left or bottom or right:
                neighbors.i.f = 10
            if top_right or top_left or bottom_left or bottom_right:
                neighbors.i.f = 14
                
        '''previous = current
        current = target
        current.parent = previous'''

