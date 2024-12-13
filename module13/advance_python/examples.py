
#example 1:
print(list(map(lambda num:num*num, [1,2,3,4,5,6,7,8,9,10])))

#example 2
from functools import reduce


nums = [1, 2, 3, 4, 5]


product = reduce(lambda x, y: x * y, nums)

print("The product of the list is:", product)



#example 3:
def is_even(num):
    return num % 2 == 0

print(list(filter(is_even, nums)))