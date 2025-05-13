#methods


lst=[]
lst.append("abc")
lst.append(123)
print(lst)

#ask from user
list=[]
while True:
    value=input("Enter the value:")
    list.append(value)
    choice=input("enter e to exit:")
    if choice.lower()=="e":
        break
    print(list)

#inserting in middle
thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)

#extend
thislist=["apple","banana","cherry"]
mylist=["kiwi","orange"]
thislist.extend(mylist)
print("thislist:",thislist)
print("mylist:",mylist)

#remove- only remove once
thislist=["apple","banana","cherry","apple"]
thislist.remove("apple")  #this removes first apple in the list
print(thislist)
thislist.remove("apple") #this removes second apple in the list
print(thislist)

#removing from index position - pop remove last value of list and if we provide index in pop we can remove any value 
thislist=["apple","banana","cherry","apple"]
thislist.pop()
thislist.pop(1)
print(thislist)

#del
thislist=["orange","banana","cherry"]
#del thislist() --- this will delete whole variable
del thislist[1]
print(thislist)

#clear
thislist=["orange","banana","cherry"]
thislist.clear() #use to make list emppty
print(thislist)











