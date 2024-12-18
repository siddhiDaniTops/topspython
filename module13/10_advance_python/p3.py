
num=[12,4,56,67,89,54,67,89,32,23,23]
def is_even(num):
    return num % 2 == 0

print(list(filter(is_even, num)))