"""Example to show how to count how many specific values are in and array.
This can be for instance used to count how many elements of given type
is in a mesh
"""
import numpy
from collections import Counter
a = numpy.array([0, 1, 0, 3, 5, 0 ,1], dtype='int64')
print(a)

# Create counter dictionary
b = Counter(a)
print(b)

# Create selector to check how man values '0' and '5' is in a
selector = [0, 5]
print(selector)

# count how many items of value in selector are in array a
z = sum(map(lambda x: x[1]*(x[0] in selector), b.items()))
print(z)
