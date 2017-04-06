class vector(object):
    def __init__(self, xaxis, yaxis):
        self.xaxis = xaxis
        self.yaxis = yaxis

def add(vector1, vector2):
    result = vector((vector1.xaxis + vector2.xaxis), (vector1.yaxis + vector2.xaxis))
    return result

def subrtract(vector1, vector2):
    result = vector((vector1.xaxis - vector2.xaxis), (vector1.yaxis - vector2.yaxis))
    return result

def multiply(vector1, scalar):
    result = vector((vector1.xaxis * scalar), (vector1.yaxis * scalar))
    return result

def magnitude(vector1):
    