from graph import Node
from graph import Graph
import math

A = Node(0, 0)

B = Node(1, 0)

C = Node(2, 0)

D = Node(0, 1)

A.parent = None
B.parent = A
C.parent = B
D.parent = A

Grid = Graph(2)

