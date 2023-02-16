"""
Regular Polygons: polysum
'n' number of sides - of a regular polygon
's' length of each side

The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon = s*n

Function 'polysum' takes 2 arguments,
'n' and 's' and returns sum the area and square of the perimeter of the regular polygon.
The result is rounded to 4 decimal places.

"""

import math

def polysum(n,s):

    numerator = 0.25*n*(s**2)
    denominator = math.tan(math.pi/n)
    polygon_area = numerator/denominator
    polygon_perimeter = (n*s)**2
    polysum = polygon_area + polygon_perimeter
    result = round(polysum, 4)
    return result

print(polysum(232,233))