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
    while current != destination:
        neighbors = get_neighbors(current, Grid)
        for i in neighbors:
            if top or left or bottom or right:
                '''Should make the value of G = 10'''
            if top_right or top_left or bottom_left or bottom_right:
                '''Should make the value of G = 14'''
        '''previous = current
        current = target
        current.parent = previous'''
