# Defines a centre of mass class, which takes a number of points, calculates their CoM, and returns a point.

import yaml

from spatial import Point, COM

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