# coding: utf-8
import math

class vector:
    def __init__(self,_v=[]):
        self.v = _v

    def __add__(self, o):
        if len(o.v) < len(self.v): o.v += [0 for x in range(len(self.v)-len(o.v))]
        elif len(o.v) > len(self.v): self.v += [0 for x in range(len(o.v)-len(self.v))]
        return [self.v[i] + o.v[i] for i in range(len(o.v))]

    def __sub__(self, o):
        return self.__add__(vector(o*-1))

    def __mul__(self, o):
        if isinstance(o,vector):
            if len(o.v) < len(self.v): o.v += [0 for x in range(len(self.v)-len(o.v))]
            elif len(o.v) > len(self.v): self.v += [0 for x in range(len(o.v)-len(self.v))]
            return sum([self.v[i] * o.v[i] for i in range(len(o.v))])
        else:
            return map(lambda x: x*o, self.v)

    def __str__(self):
        return str(self.v)

    def __abs__(self):
        return math.sqrt(sum([x**2 for x in self.v]))
