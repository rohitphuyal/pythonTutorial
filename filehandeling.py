# #reading the  file
# f = open("demofile.txt")
# print(f.read())

# #or change the slash to backslash------reading the file from another approach

# f = open("C:/Users/Rohit/Desktop/Basic/demofile.txt")
# print(f.read())

# #assigning the file into variable
# f = open("C:/Users/Rohit/Desktop/Basic/demofile.txt")
# value=f.read()
# print(type(value))


# #reading the some text
# f = open("C:/Users/Rohit/Desktop/Basic/demofile.txt")
# value=f.read()
# print(value)

# #first method
# print(value[7:14])
# print(value[48:55])
# print(value[-10:-6])


# #second method
# lst=value.split()
# print(lst[1])
# print(lst[8])
# print(lst[-2])


# readline method
# f = open("C:/Users/Rohit/Desktop/Basic/demofile.txt")
# row1=f.readline()
# row2=f.readline()
# print(row1)
# print(row2)
# print(type(row1))
# print(type(row2))
# print(row1[7:14])
# print(row2[7:14])

# #readline next method to read line at a time using loop
# f = open("C:/Users/Rohit/Desktop/Basic/demofile.txt")
# for x in f:
#     print(x)

# #readlines
# f = open("C:/Users/Rohit/Desktop/Basic/demofile.txt")
# value=f.readlines()
# print(value)
# new_value=[x.strip("\n") for x in value]
# print(new_value)






