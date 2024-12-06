
string_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(string_list)
search_string = input("search string ?   :")

# Using a for loop and if condition to find the string
found = False
for string in string_list:
    if string == search_string:
        print(search_string, "it found in list ..")
        found = True
        break
    else:
       print(search_string," not found in the list.")
       break
