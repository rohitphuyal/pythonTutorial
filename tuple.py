
#checking tuple and list 
fruits=("apple", "orange")
print(type(fruits)) #checking types for the given question
lst=[1]
print(type(lst)) #hecking type

#loop for tuple
tup=(1,2,3,4)
for x in tup:
    print(x)

for x in range(len(tup)):
    print(tup[x])


#converting tuple into list and list into tuple
x=("apple","banana","cherry")
y=list(x) #converting tuple into lists
x=tuple(y) #converting lists into tuple again


#unpacking tuple
fruits=("apple","banana","cherry")
red,yellow,pink=fruits
print(red)


#assigning tuple into single variable
fruits=("apple","banana","cherry","strawberry","raspberry")
green,yellow,*red=fruits
print(green)
print(yellow)
print(red) 