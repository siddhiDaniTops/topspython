#example 2
from functools import reduce


nums = [1, 2, 3, 4, 5]


product = reduce(lambda x, y: x * y, nums)

print("The product of the list is:", product)