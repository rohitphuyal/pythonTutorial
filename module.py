def greeting(name):
    print("Hello, " + name)

def sum(a,b):
    result=a+b
    print("Result:", result)
    return result

def diff(a,b):
    result=a-b
    print("Result:", result)
    return result

def mul(a,b):
    result=a*b
    print("Result:", result)
    return result


#others cannot import or access this file if the below code is written
if __name__ =="__main__":
    print("This is calculator")
