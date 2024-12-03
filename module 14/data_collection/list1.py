#ssimple store maltipule data type
print("example 1")
list=[12,78.90,45,"siddhi","python"]

print(list)
print()
#index print
print("index value")
print(list[0])
print(list[1])
print(list[-5])
print(list[-1])
print()


#example2
print("example 2")
print(len(list))


#insert()
print("opretion in list")
print("append")
list2=[45,89,"dani","tops"]
print(list2)
list.append(list2)
print(list)
print()
print("insert")
list.insert(3,list2)#index 3 store object
print(list)
print()
 

print("delete element:.....")
print()
print("delete index -4")
del(list[-4])
print(list)
print("delete indext -1")
del(list[-1])

print(list)
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


