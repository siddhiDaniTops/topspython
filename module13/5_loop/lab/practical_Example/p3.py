
str = ["apple", "banana", "cherry", "date", "fig", "grape"]
print(str)
search = input("search string ? :")

for item in str:
    if  item == search:
        print(search, "it found in list ..")
        break
    else:
       print(search," not found in the list.")
       
