from __future__ import division


class CoordinatesDistance():

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    
    '''
    coor1(Xa, Ya)
    coor2(Xb, Yb)
    distance = under root[ sqr(Xb - Xa) + sqr(Yb - Ya)]

    '''
    def distance(self):
        step1 = ( self.coor2[0] - self.coor1[0] ) ** 2
        step2 = ( self.coor2[1] - self.coor1[1] ) ** 2
        step3 = step1 + step2
        step4 = step3 ** 0.50

        return step4

    '''
    coor1(Xa, Ya)
    coor2(Xb, Yb)
    slope = (Yb - Ya) / (Xb - Xa)
    '''
    def slope(self):
        step1 = self.coor2[1] - self.coor1[1]
        step2 = self.coor2[0] - self.coor1[0]
        step3 = step1 / step2
        return step3

coordinate1 = (3,2)
coordinate2 = (8,10)
calc_dis = CoordinatesDistance(coordinate1, coordinate2)
print ('Distance: {}'.format(calc_dis.distance()))
print ('Slope: {}'.format(calc_dis.slope()))


print ('*******************************************************************')

class Cylinder():
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius


    '''
    formula: Pi * sqr(r)h
    '''
    def volume(self):
        return self.pi * (self.radius ** 2) * self.height
    

    '''
    Formula: 2Pi * sqr(r) + 2Pi * r * h
    '''
    def surface_area(self):
        global pi
        step1 = 2 * self.pi * (self.radius ** 2)
        step2 = 2 * self.pi * self.radius * self.height
        return step1 + step2


cylinder = Cylinder(2, 3)
print ('Cylinder volume: {}'.format(cylinder.volume()))
print ('Cylinder surface area: {}'.format(cylinder.surface_area()))



