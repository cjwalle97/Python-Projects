from vector import vector

class agent(object):
    def __init__(self, position):  
        self.position = position
        self.header = None
        self.mass = 1
        self.velocity = [0, 1]
        self.force = None

def seek(agent, goal):
    if agent.position
