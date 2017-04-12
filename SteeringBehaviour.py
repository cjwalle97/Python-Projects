from pygame import time
from vector import vector
from vector import magnitude
from vector import normalize

class agent(object):
    def __init__(self, position):  
        self.position = position
        self.heading = None
        self.mass = 1
        self.velocity = vector(0, 1)
        self.force = None

class clock():
    def __init__(self):
        self.c = time.Clock()
        self.deltatime = self.c.tick(30) / 1000.0

def seek(agent, goal):
    '''Moves the agent towards a designated Vector'''
    time = clock()
    maxvelocity = 1
    v = normalize(goal - agent.position) * maxvelocity
    force = v - agent.velocity
    agent.velocity += force * time.deltatime
    agent.position += agent.velocity * time.deltatime
    agent.heading = normalize(agent.velocity)
    return force
    
def flee(agent, goal):
    '''Moves the agent'''
    time = clock()
    maxvelocity = 1
    v = normalize((agent.velocity - goal)) * maxvelocity
    force = v - agent.velocity
    agent.velocity += force * time.deltatime
    agent.position += agent.velocity * time.deltatime
    agent.heading = normalize(agent.velocity)
    return force

def wander():
    

def main():
    '''main'''
    a = agent(vector(3, 3))
    print a.position
    test1 = seek(a, vector(4,4))
    print test1
    test2 = flee(a, vector(-5,-5))
    print test2
    #d

if __name__ == '__main__':
    main()
