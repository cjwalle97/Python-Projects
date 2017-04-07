import math

class vector(object):
    def __init__(self, xaxis, yaxis):
        self.xaxis = xaxis
        self.yaxis = yaxis
    def __str__(self):
        '''overload string for print'''
        return str(self.xaxis) + ', ' + str(self.yaxis)

    def __add__(self, other):
        result = vector((self.xaxis + other.xaxis), (self.yaxis + other.xaxis))
        return result

    def __sub__(self, other):
        result = vector((self.xaxis - other.xaxis), (self.yaxis - other.yaxis))
        return result


    def __mul__(self, scalar):
        result = vector((self.xaxis * scalar), (self.yaxis * scalar))
        return result


    def __div__(self, other):
        result = vector((self.xaxis / other.xaxis), (self.yaxis / other.yaxis))
        return result

    def dot_product(self, other):
        result = (self.xaxis * other.xaxis) + (self.yaxis * other.yaxis)
        return result

def magnitude(vector):
    total = (vector.xaxis * vector.yaxis)
    result = math.sqrt(total)
    return result

def normalize(vector1):
    result = vector((vector1.xaxis / magnitude(vector1)), (vector1.yaxis / magnitude(vector1)))
    return result

def main():
    a = vector(5,5)
    b = vector(3,3)

    c = a + b

    d = a - b

    e = a * 5

    f = a / b

    g = magnitude(a)

    h = normalize(a)

    i = a.dot_product(b)

    tests = [c, d, e, f, g, h, i]
    for j in tests:
        print j

if __name__ == '__main__':
    
    main()