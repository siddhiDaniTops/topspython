def integer_iterator(integers):
    for num in integers:
        yield num

numbers = [1, 2, 3, 4, 5]
iterator = integer_iterator(numbers)
   
for num in iterator:
        print(num)        