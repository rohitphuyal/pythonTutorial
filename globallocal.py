#global and local variable concept
num1=10
num2=20
def addition(z,y=1):
    global x
    x=10
    print(num1)
value=addition(num1,num2)
print(x)

#args ---- for addition
def addition(*args):
    print(args)
    print(type(args))
    sum=0
    for x in args:
        sum=sum+x
    print("result:", sum)
        
addition(1,2,3,4,5)


#args -- for subtraction
def diff(*args):
    print(args)
    print(type(args))
    difference=args[0]
    for x in range(1,len(args)):
        difference=difference-args[x]
    print("diff result:", difference)
        
diff(1,2,3,4,5)

