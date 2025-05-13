#raise custom exception to handle different cases with same except block
x=int(input("enter age:"))
try:
    if x>100:
        raise Exception("sorry, no numbers above 100")
    elif x==0:
        raise Exception ("sorry, age is zero")
except Exception as e:
    print(e)
    x=int(input("Re-enter Age:"))

#different exception 
# class negative_error(Exception):
#     def __init__(self,message):
#         super().__init__(message)
# class zero_error(Exception):
    #complete this