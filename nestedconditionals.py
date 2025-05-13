x=5
if x>0:
    if x<10:
        print("x is positive single digit number")
    else:
        print("x is positive number, but not a single digit")
else:
    print("x is not a positive number")

#simplified
x=5
if x>0 and x < 10:
    print("x is positive single digit number")

else:
    print("x is a positive number")


#from user input simplified from above
#simplified
x=int(input("Enter first number"))
if x>0 and x<10:
    print("x is positive single digit number")
else:
    print("x is a positive number")