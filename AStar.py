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

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 25
COLS = 25
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]