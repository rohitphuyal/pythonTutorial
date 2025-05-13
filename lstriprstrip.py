s= "              Hello World       "
print(s.lstrip())
print(s.rstrip())


a= "     Hello Rohit   "
x=a.strip()
x=x+"abc"
print(x)
print(a.strip())

#1
name=["hello", "world", "python"]
output="".join(name)
print(output)

#2
value="12345"
print(value.isdigit())

#3
name="HELLO"
print(name.isupper())
print(name.islower())

#split
name="hello#world#Ram"
out=name.split("#")
print(out)

#format old one
x=int(input("Enter first num"))
y=int(input("Enter second num"))
result=x+y
print("sum of () and () is:".format(x,y), result)

#same for for- now people use f string
x=int(input("Enter first num"))
y=int(input("Enter second num"))
result=x+y
print(f"sum of (x) and (y) is :", result)


#question
data="############Hello######World######"
strip_data=data.strip("#")
print(strip_data)
value=strip_data[0:5] + " " + strip_data[11:]
print(value)


#question
data="Hello World"
output= "####hello####world####"

first_output=data.split()
second_output="####".join(first_output)
third_output=second_output.lower()
print(third_output)
total_length=len(output)
lside_length=total_length-len(output.lstrip("#"))
rside_length=total_length-len(output.rstrip("#"))

  



