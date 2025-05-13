#for multiple line use three quotes """ or ''', for single line use  single quote "" or ''
name="Rohit"
name1="Rohit's" #or
name2="Rohit\'s"
print(name)
print(name1)


#Indexing
a=("Hello, Rohit")
print(a[0])
print(a[-1])

#Slicing - it prints the value of start and end
s="Hello, World"
print(s[7:12]) #or
print(s[7:0]) #or
print(s[-1:-5]) #or
print(s[7:])

#skipping
s="Hello, World"
print(s[0:-1:2])

#example
name="rar"
reverse= name[::-1]
print(reverse)
if name==reverse:
    print("This is palindrome")



