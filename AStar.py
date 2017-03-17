#from drawablenode import DrawableNode
from graph import Node
#from graph import Graph
import math
import pygame


A = Node(0, 0)

B = Node(1, 0)

C = Node(2, 0)

D = Node(0, 1)

A.parent = None
B.parent = A
C.parent = B
D.parent = A

NodeList = list(Node)

NodeList.insert(0, A)
NodeList.insert(1, B)
NodeList.insert(2, B)
NodeList.insert(3, C)
NodeList.insert(4, D)

