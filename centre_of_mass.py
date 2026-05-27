# defines a point class, according to lat, long, altitude, and a weight.
# defines a centre of mass class, which takes a number of points, calculates their CoM, and returns a point.

from numpy import arccos, arctan2
from math import sin, cos, radians, degrees, sqrt
import yaml

radius_earth = 6371e3

class Point():

    def __init__(self, lat, lon, alt=0, weight=1):
        
        if(lat>90 or lat<-90): raise ValueError('Latitude must be in range [-90,90].')
        if(lon>=180 or lon<-180): raise ValueError('Longitude must be in range [-180,180].')

        self.theta = radians(90-lat)
        self.phi = radians(lon)

        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.rad = radius_earth + alt
        self.weight = weight

        self.x = self.rad * sin(self.theta) * cos(self.phi)
        self.y = self.rad * sin(self.theta) * sin(self.phi)
        self.z = self.rad * cos(self.theta)

    def __str__(self):
        return (
            f"Lat:    {self.lat:.3f} deg\n"
            f"Lon:    {self.lon:.3f} deg\n"
            f"Alt:    {self.alt:.0f} m"
        )

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

def main():

    with open('locations.yaml', 'r') as f:
        locations = yaml.load(f, Loader=yaml.SafeLoader)

    # Set points from config
    points = [Point(**locations[location]) for location in locations.keys()]

    # Calculate COM:
    c = COM()
    for point in points:
        c.add_point(point)

    print('COM:')
    print(c.get_com())

if __name__ == "__main__":

    main()