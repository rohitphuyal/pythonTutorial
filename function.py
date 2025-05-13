#function---- reuseable of code
#type 1 no return and parameter less
def addition():
    result=1+2
    print(result)
addition()

#type 2
def addition(x,y):
    result=x+y
    print(result)
addition(1,2)
addition(4,2)

#type 3 : return and parameter----most used type
def addition(x,y):
    result=x+y
    return result
final1=addition(1,7)
final2=addition(5,2)
print(final1)
print(final2)

#function ----ask from user
def addition(x,y):
    result=x+y
    return result
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
final3=addition(a,b)
print("The addition is:",final3)


#subtraction
def subtraction(x,y):
    result=x-y
    return result
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
final4=subtraction(a,b)
print("The subtraction is:",final4)

#multiplication
def multiplication(x,y):
    result=x*y
    return result
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
final5=multiplication(a,b)
print("The multiplication is:",final5)

#division
def division(x,y):
    result=x/y
    return result
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
final6=division(a,b)
print("The division is:",final6)

#modulus
def modulus(x,y):
    result=x%y
    return result
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
final6=modulus(a,b)
print("The modulus is:",final6)

#exponential
def exponential(x,y):
    result=x**y
    return result
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
final7=exponential(a,b)
print("The exponential is:",final7)

#next process -----using if elif else conditions


#returing multiple values from functions
def stats(num):
    max1=max(num)
    min1=min(num)
    sum1=sum(num)
    return max1,min1,sum1
number=[1,2,3,4,5]
result=stats(number)
print(result)
print(type(result))








