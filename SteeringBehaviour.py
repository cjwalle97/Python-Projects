from vector import vector

class Agent(object):
    def __init__(self, position):  
        self.position = position
        self.direction = None
        self.mass = 1
        self.velocity = [0, 1]
        self.force = None

def seek(location):
    