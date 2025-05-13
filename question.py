#for loop
#count from 0-10 skip 6
#sum=0+1+2+3+4+5+7+8+9
count=0
sum=0
for x in range(10):
    if x!=6:
        print("Counting",x)
        count=count+1
        sum=sum+x
print("Total count",count)
print("result", sum)


#incase of while loop
count=0
while True:
    print(count)
    count +=1
    choice= input("Enter e for exit else any number:")
    if choice =="e":
        print("exiting")
        break
print("total sum of count", count)


#to print pyramid structure using loops -use the logic of rows a nd column.
#1
#12
#123
#1234
#12345

for r in range(6):
    for c in range(r):
        print(c+1, end="")
    print("")   #this denotes to go in neext step/line 