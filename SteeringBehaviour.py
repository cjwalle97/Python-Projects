import pygame
from vector import vector
from vector import magnitude
from vector import normalize

class agent(object):
    def __init__(self, position):  
        self.position = position
        self.heading = None
        self.mass = 1
        self.velocity = [0, 1]
        self.force = None

class clock():
    def __init__(self):
        self.c = game.time.clock()
        self.deltatime = self.c.pygame.time.tick(30) / 1000.0

def seek(agent, goal):
    maxvelocity = 1
    v = normalize((goal - agent.position)) * maxvelocity
    force = v - agent.velocity
    agent.velocity += force * deltatime


'''def flee(agent, goal):'''