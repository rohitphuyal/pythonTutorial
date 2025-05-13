"""
1.display list
2.update list
3.insert at end of list
4.insert at any position that user give to list
5.delete elememt of list as user give the value that need to be deleted
6.delete the last element of list
7.clear list
8.Delete entire list
9.Remove only duplicate values from list

"""

list=["ram","shyam","hari","gopal","ram"]
print(list)
list[1]="Rohit"
print(list)
list.insert(5, "Ramesh")
print(list)
value=int(input("Ask from user:"))
list.append(value)
