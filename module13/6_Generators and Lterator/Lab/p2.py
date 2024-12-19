def num_iterator(integers):
    for num in integers:
        yield num

num = [1, 2, 3, 4, 5]
iterator = num_iterator(num)
   
for num in iterator:
        print(num)        