#question 1
#Value= take input from user
#if "hello" print ("there is hello in value")


x= input("Type anything:")
if "hello" in x or "Hello"in x:
    print("There is hello in X")

#question 2
#Value= take number input from user
#if number is positive and greater than 100 (print above 100)
#if number is zero print("number is zero")
#if number is negative and less than -10 ("print number is less than -10")

x= int(input("Enter the first number:"))
if x>100:
    print("above 100")
elif x==0:
    print("The number is zero")
elif x<0 and x<-10:
    print("x is less than -10")

#question 4 (mistake) do again
#value = take input from user

a=int(input("first number"))
if a%2!=0:
    print("a is odd")
else:
    print("a is even")