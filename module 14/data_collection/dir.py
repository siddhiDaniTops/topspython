
#example 1
stud={
        "id" :101,
        "name":"siddhi",
        "cours":"bca",
        "city":"surat"

       }
print(stud)
#example 2
print("cours:",stud["cours"])
print("id :",stud["id"])
print("name :",stud["name"])

#example 3
stud["name"] = "siddhi"
s={6,9,0}
h={"jjk","ghj","kh"}
print()
print("hiiiiiii",stud.items)
print(stud.fromkeys(s, h))#keys and value
#example 4
keys = stud.keys()
values = stud.values()
print(keys)
print(values)


#example 5
L1 = [1,2,3,4,5, 6,7,8,9]
L2 = [11,22,33,44,55]
L3 = [10,20,30,40,50]

list1=L1+L2+L3
for key, value in stud.items():
    print(key,":", value)

for dir1 in dir(list1):
    print(dir1)
  

#example 6

    users = []
flag = True
while flag:
    user = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: "))
    }
    users.append(user)
    choice = input("Do you want to add more users? (yes/no): ") 

    print(users)
    if choice.lower() == "yes":
        flag = True
    else:
        flag = False