#importing from module
#method to import whole file
#custom packages
import module as m
m.greeting("Rohit")
final=m.sum(1,2)

#method
from module import sum
result=sum(3,4)

from module import diff
difference=diff(5,4)


#decorator
#without parameter function and without parameter decorator
def decorator1(x):
    def wrapper():
        print("Something before function runs")
        print("Start time")
        x()   #say_hello()
        print("end time-start time")
    return wrapper

@decorator1
def say_hello():
    print("Hello")

say_hello()


@decorator1
def say_hi():
    print("Hi")

say_hi()



#with parameter function and without parameter decorator
def decorator1(fun): #fun= say_hello
    def wrapper(*args, **kwargs):
        print("Something before function runs")
        print("Start time")
        fun(*args, **kwargs)  #say_hello()
        print("end time-start time")
    return wrapper

@decorator1
def say_hello(x,y):
    print("Hello",x,y)

say_hello("Raj", "sup?")


#with parameter function and parameter decorator
def great_decorator(greetings): #greeting - Hello
    def decorator1(fun): #fun- say_hello
        def wrapper(*args, **kwargs):
            print(f"{greetings} before function runs")
            fun(*args, **kwargs)
            print("something after the function runs")
        return wrapper
    return decorator1
@great_decorator("hello")
def say_hello(a,b):
    print("a and b", a,b)

say_hello(1,2)   





