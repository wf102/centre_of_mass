# defines a point class, according to lat, long, altitude, and a weight.
# defines a centre of mass class, which takes a number of points, calculates their CoM, and returns a point.

from numpy import arccos, arctan2
from math import sin, cos, radians, degrees, sqrt
from statistics import mean

radius_earth = 6371e3   # in meters

class Point():

    def __init__(self, lat, long, alt, weight=1):
        
        if(lat>90 or lat<-90):      raise ValueError('Latitude must be in range [-90,90].')
        if(long>=180 or long<-180): raise ValueError('Longitude must be in range [-180,180].')

        self.theta = radians(90-lat)
        self.phi = radians(long)

        self.lat = lat
        self.long = long
        self.alt = alt
        self.rad = radius_earth + alt
        self.weight = weight

        self.x = self.rad * sin(self.theta) * cos(self.phi)
        self.y = self.rad * sin(self.theta) * sin(self.phi)
        self.z = self.rad * cos(self.theta)

    def __str__(self):

        return f'({self.lat}, {self.long}, {self.alt}, {self.weight})'
    
    def __add__(self, other):

        return Point(self.x+other.x, self.y+other.y, self.z+other.z, self.weight+other.weight)

class COM():

    def __init__(self):
        self.points = []

    def add_point(self, new_point):
        return self.points.append(new_point)

    def get_com(self):

        if len(self.points) == 0: return None

        sum_weight = sum([point.weight for point in self.points])

        x = sum([point.x*point.weight for point in self.points])/sum_weight
        y = sum([point.y*point.weight for point in self.points])/sum_weight
        z = sum([point.z*point.weight for point in self.points])/sum_weight

        r = sqrt(x**2 + y**2 + z**2)
        theta = arccos(z/r)
        phi = arctan2(y,x)

        lat = degrees(radians(90) - theta) 
        long = degrees(phi)
        alt = r-radius_earth

        return Point(lat, long, alt, sum_weight)


# define points:
p_turkdean = Point(51.895846, -2.114565, 0)
p_rosewood = Point(51.898005, -2.104593, 0)
p_witney   = Point(51.779955, -1.490665, 0)
p_bristol = Point(51.453309, -2.588483, 0)
p_paris = Point(48.85989398981465, 2.2352585254318944, 0)
p_baltimore = Point(39.28836948143914, -76.62152303086647, 0)
p_bangalore = Point(12.973712960117666, 77.58698644923022, 0)
p_hongkong = Point(22.311170317382366, 113.68675044868934, 0)

# calculate COM:
c = COM()
c.add_point(p_turkdean)
#c.add_point(p_rosewood)
#c.add_point(p_witney)
#c.add_point(p_bristol)
c.add_point(p_bangalore)
c.add_point(p_hongkong)
c.add_point(p_paris)
c.add_point(p_baltimore)

print('COM:')
print(c.get_com())