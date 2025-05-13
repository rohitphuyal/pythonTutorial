#iterations
#for loop
for x in range(10): # 0-9(Its ten times)
    print("Hello")


#while loop
x=0
while x<10:
    print("hello")
    x=x+1

#print if the value is odd or even and resulting their total count(for loop)
odd_count=0
even_count=0
for x in range(10):
    if x%2!=0:
        print("x is odd:",x)
        odd_count= odd_count +1
    else:
        print("its even:",x)
        even_count= even_count+1
print("Total odd count:", odd_count)
print("Total even count:", even_count)


#if we want to run in between numbers in range
for x in range(10,20):
    print(x) #it  prints from 10 to 19. includes 10 but not 20

#if we give in range next parameter it will jump which is also mean scape. eg. if (10,20,3)= it will jump two times and print result like 10,13,16,19
for x in range(10,20,3):
    print("jump",x)


#for string
name="abcde"
for x in name:
    print("string", x)
    

#for odd through range
for odd in range(11,20,2):
    print("odd numbers",odd)






#while loop
count=0
while count<10:
    print(count)
    count= count+1

#for odd and even
x = 0
odd_count = 0
even_count = 0

while x < 10:
    if x % 2 != 0:
        print("x is odd:", x)
        odd_count= odd_count+1
    else:
        print("it's even:", x)
        even_count= even_count+1
    x=x+ 1  # Increment x to avoid infinite loop

print("Total odd count:", odd_count)
print("Total even count:", even_count)

#for swap we have to make temp while is new variable to store value
#question
#x=10
#y=20
#print(x)=20
#print(y)=10
#x,y=y,x

x=10
y=20
temp= x #temp=10
x=y #x=20
y=temp #y=10
print(x)
print(y)

#next method
x=5
y=6
x=x+y #5+6=13
y=x-y #5-6= -1
x=x-y
print(x)
print(y)













