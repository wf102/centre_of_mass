# Centre of mass calculator

This simple tool calculates the centre of mass of a number of objects (eg people) across the globe.
Each body is specified by a latitude, longitude, and altitude, and can additionally be given a weight.

The motivation came from a discussion with four friends spread across the globe, in which we wondered where our centre of mass would be.
Our five locations were Cheltenham, Paris, Baltimore, Bangalore, and Hong Kong, and have been added via the `locations.yaml` config file.

The script `centre_of_mass.py` reads the configuration, creates five point objects, and calculates their centre of mass (in latitude, longitude, and altitude).

The centre of mass for this particular configuration happens to be in a field near a rural village ~350km north of Moscow (and also 2245.8 km underground).

Output:
```
Lat:    59.080 deg
Lon:    39.102 deg
Alt:    -2245812 m
```

### Note of caution:

The centre of mass is the point in 3d space that minimises the sum of squares of the Eulidean distances to all constituent points.
The projection of this point onto the surface (ie zero altitude) should not be confused with the point that minimises the sum of squares of the geodesic distances, which might be considered the fairest location to meet up.
For this we'd need to calculate the [Fréchet mean](https://en.wikipedia.org/wiki/Fr%C3%A9chet_mean).
However if minimising total travel time or fuel were the priority we'd need to minimise the sum of the geodesic distances, for which we'd need to calculate the geodesic median.
