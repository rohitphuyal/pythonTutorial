"""
1.create empty tuple
2.create the tuple with single value inside it
3.unpack tuple into three variable
4.if you have tup=(1,2,3) add 4 inside it
5.if you have tup=(1,1,1,2,3,3) count value 1
6.create empty set
7.remove duplicate value from set
8.add values to set by asking to user
9.if you have set ={1,2,3,4,5} update 3 to 6 (i.e. output should be set ={1,2,6,4,5})
10.create the set of 100 from 1-100 and pick random number from set each time

"""

tup=()
print(type(tup)) #1
tup1=("Rajesh",) # to create single value in tuple we have to add comma after it 
print(type(tup1)) #2
tup3=("apple","banana","orange","strawberry") #3
red,yellow,orange,pink=tup3
print(red)
print(yellow)
print(orange)
print(pink)

tup1=(1,2,3) #4
tup2=(4,)
tupall=tup1+tup2
print(tupall)

tup5=(1,1,1,2,3,3) #5
count=tup5.count(1)
print(count)

set1=set()  #5
print(type(set1))
print(set1)


#question10
set1=set()
for x in range(1,101):
    set1.add(x)
print(set1)
while True:
    choice=int(input("Do you want to pick random number if yes press 1:"))
    len_element=len(set1)
    if choice== 1 and len_element!=0:
        pop_number=set1.pop()
        print(pop_number)
    elif len_element==0:
        print("set is empty")
    else:
        print("Exiting............")
        break        



