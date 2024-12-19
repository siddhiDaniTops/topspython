def generate_even_numbers():
    num = 0
    count = 0
    while count <=10:
        yield num
        num += 2
        count += 1
even_numbers = generate_even_numbers()

for even in even_numbers:
    print(even)
