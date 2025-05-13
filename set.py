set1={"apple","banana","cherry","banana"}
print(set1)

set2={}
print(type(set2)) #checking data typpes

#for empty set
set1=set()
print(type(set1))
print(set1)

#for loop
set1={1,2,3}
for x in set1:
    print(x)

#converting set into tuple and list
set1={1,2,3,4}
lst=list(set1)
print(lst)

#Adding the set with add method
thisset={"apple","orange","cherry"}
thisset.add("banana")
print(thisset)

#updating the set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)

#remove set method
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#discard method
fruits = {"apple", "banana", "cherry"}

fruits.discard("strawberry")

print(fruits)


#pop method in set
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

