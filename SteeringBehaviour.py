from pygame import Clock
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
        self.c = Clock()
        self.deltatime = self.c.tick(30) / 1000.0

def seek(agent, goal):
    if agent.position == goal:
        return 0
    time = clock()
    maxvelocity = 1
    v = normalize((goal - agent.position)) * maxvelocity
    force = v - agent.velocity
    agent.velocity += force * time.deltatime
    agent.position += agent.velocity * time.deltatime
    agent.heading = normalize(agent.velocity)
    return force
    
'''def flee(agent, goal):'''


def main():
    '''main'''
    a = agent(vector(3, 3))
    b = seek(a, vector(4,4))
    c = seek(a, vector(3,3))

if __name__ == '__main__':
    main()
