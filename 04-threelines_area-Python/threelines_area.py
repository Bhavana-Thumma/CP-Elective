# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a, b, c):
    t = (a+b+c)/2
    return int(math.sqrt((t*(t-a)*(t-b)*(t-c))))

	
