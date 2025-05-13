s="Hello World"
s="Hi" + s[-5:]
print(s)


#replace
s="Hello World"
print(s.replace("World", "Python"))
print(s)

#replacing actually
s=("hello ")
s=s.replace("hello", "Hi World")
print(s)
print(s.count(s))


#checking the capital and small using string method
name= input("Enter the string")
count=0
print("string", name)
value= input("Enter which value you want to count:")
for i in range(len(name)):
    if name[i].lower()==value.lower():
        count +=1 
print("count values for", value, ":", count)