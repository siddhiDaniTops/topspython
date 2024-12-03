#ssimple store maltipule data type
print("example 1")
list=[12,78.90,45,"siddhi","python"]
list2=["me",1,2+3,90.89]
print(list)
print("index 4")
print(list[4])
print()


#example2
print("example 2")
print(len(list))
print()

#example 3
print("example 3")
print("insert....")
list[-1] = list.insert(-1,"danidhariya")
print(list)
print(list[1:4])
print("index 4")
print(list[4])
print()
print("append....")
list.append(list2)
print(list)
print(list[1:4])
print("index 4")
print(list[-1])
print()

#example 4

#pop
print("pop....")

list.pop()
print(list)
print()
#remove
print("remove....")
list.remove("siddhi")
print(list)
print()

