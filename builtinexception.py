 #error handling
#type 1
# try:
#     x=int(input("First number:"))
#     y=int(input("Second number:"))
#     result=x/y
#     print("result", result)
# except ZeroDivisionError as e:
#     print(e)
#     print("You have entered zero value number")
#     x=int(input("First number:"))
#     y=int(input("Second Number:"))
#     result=x/y
#     print("Result",result)

# except TypeError as e:
#     print(e)
#     print("You have entered the character instead of number")
#     x=int(input("First number:"))
#     y=int(input("Second Number:"))
#     result=x/y
#     print("Result",result)

# except ValueError as e:
#     print(e)
#     print("You have entered the wrong value")
#     x=int(input("First number:"))
#     y=int(input("Second Number:"))
#     result=x/y
#     print("Result",result)


#recursive 
def division():
    try:
        x=int(input("First number:"))
        y=int(input("Second number:"))
        result=x/y
        print("result", result)
    except ZeroDivisionError as e:
        print(e)
        print("You have entered zero value number")
        division()

    except TypeError as e:
        print(e)
        print("You have entered the character instead of number")
        division()

    except ValueError as e:
        print(e)
        print("You have entered the wrong value")
        division()
division()


#exception with single exception case
def division():
    try:
        x=int(input("First number:"))
        y=int(input("Second number:"))
        result=x/y
        print("result", result)
    except Exception as e:
        print(e)
        division()
division()




