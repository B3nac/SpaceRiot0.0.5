import pygame as pg
import copy

class Vector(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def add(self, other): 
        self.x += other.x
        self.y += other.y
        
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        
    def mul(self, value):
        self.x *= value
        self.y *= value
        
    def div(self, value):
        if not value == 0:
            self.x /= value
            self.y /= value
            
    def mag(self):
        a = self.x**2.0
        b = self.y**2.0
        c = math.sqrt(a + b)
        return c
        
    def norm(self):
        magnitude = self.mag()
        self.div(magnitude)
        
    def __str__(self):
        return format("x=%r,y=%r" % (self.x,self.y))

    def get_copy(self):
        return copy.copy(self)


        
