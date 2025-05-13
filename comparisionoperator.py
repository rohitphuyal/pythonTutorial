#Comparision Operator for equal
x=1
y=2
print("1==2:",x==y) # ==

#For not equal !=
x=1
y=2
print("1!=2:", x!=y) 

#Can do equal and not equal operator for string also
a="Ram"
b="Hari"
print("Ram==Hari",a==b)
print(a!=b)

#Greater than and less than
h=9
z=7
print(h>z)
print(h<z)

#Logical Operator (AND)
x=1
y=2
z=3
print("results:", x<3 and y<3 and z<=3)
print("Is x greatest of all:", x>y and x>z)


#Logical Operator (OR)
x=1
y=2
z=3
print("Is x greatest of all:", x>y or x>z)

x=0
#x is positive

print("Is x positive:", x==0 or x>0)


# combining AND operator and OR operator

print((x>=0 and y>=0) or z<0)

#Printing NOT: it means opposite
print(not x>=0)


#Identity Operator

x=[1,2,3,4]
y=[1,2,3,4]
print("Checking equals:", x==y)
print("Location check:", x is y) #This checks the location of value stored
print(x is not y)

#Membership Operator

x="Hello"
y=[1,2,3]
print("h" in x)

#Assignment Operator
x=2
x +=5
print(x)




