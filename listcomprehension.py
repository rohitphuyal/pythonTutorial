#list comprehension ---for shortcut method
fruits=["apple","banana","kiwi","cherry","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

#change apple to banana while printing
fruits=["apple","orange","cherry","apple","mango","apple"]
newlist=["banana" for x in fruits if "apple" in x]
print("changed to banana:", newlist)

#conversion to uppercase
fruits=["apple","banana","kiwi","cherry","mango"]
newlist=[x.upper() for x in fruits]
print("uppercase:", newlist)

#list comprehension for if else
fruits=["apple","orange","cherry","apple","mango","apple","banana"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print("The result:",  newlist)

number=[1,2,3,4,5,6,7,8,9]
newlist=["even" if x%2==0 else "odd" for x in number]
print("print odd even:", newlist)


#sorting number  --- sort 
num=[100,1,5,8,0]
num.sort() #ascending
print(num)
num.sort(reverse=True) #descending
print(num)

#sorted ----- this is best to use than sort
thislist=["orange","mango","cherry"]
newlist=sorted(thislist) #ascending
print(newlist)
newlist=sorted(thislist, reverse=True) #descendding
print(newlist)

#deep copy



