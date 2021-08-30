"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math
def binary_search(input_array, value):
    # Your code goes here
    temp = input_array
    while len(input_array) >= 1:        
	    n = len(input_array) 
	    middle_element = input_array[math.floor(n/2)]  
	    if value == middle_element:
	    	return temp.index(middle_element)
	    elif value < middle_element:
	    	input_array = input_array[:math.floor(n/2)]
	    elif value > middle_element:
	       input_array = input_array[math.floor(n/2)+1:]
    return -1