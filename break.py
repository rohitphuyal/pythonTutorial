#break comes with loop not useful in for loop
for x in range(10):
    if x==4:
        break
    print(x)


#while loop- break is useful
count=0
while count<10:
    if count ==5:
        break
    print("While break",count)
    count=count+1