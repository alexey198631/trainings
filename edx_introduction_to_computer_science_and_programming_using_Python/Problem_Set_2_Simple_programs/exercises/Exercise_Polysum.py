"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s.
This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
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