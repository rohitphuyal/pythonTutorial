#default function for addition
def addition(x,y=1):
    final=x+y
    return final
num1=10
num2=20
value=addition(num1,num2)
print(value)

#default function for subtraction
def subtraction(x,y,z=10):
    final=x-y-z
    return final
num1=10
num2=20
value=subtraction(num1,num2)
print("The subtract is:",value)


#next example for default value
def greet(name, greeting="Hello"):
    """
    Greets a person with an optional custom greeting.
    """
    print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi")  # Output: Hi, Bob!
