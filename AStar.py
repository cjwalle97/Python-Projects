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
    
        previous = current
        current = target
        current.parent = previous

