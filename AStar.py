from drawablenode import DrawableNode
from graph import Node
from graph import Graph
import math
import pygame

Grid = Graph(2)

A = Grid.get_node(Node(0, 0))

B = Grid.get_node(Node(1, 0))

C = Grid.get_node(Node(2, 0))

D = Grid.get_node(Node(0, 1))

A.parent = None
B.parent = A
C.parent = B
D.parent = A

ADrawn = DrawableNode(A)

BDrawn = DrawableNode(B)

CDrawn = DrawableNode(C)

DDrawn = DrawableNode(D)

ADrawn.color(255, 255, 255)
