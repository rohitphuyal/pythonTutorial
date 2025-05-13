
#for calculation of len it starts from 1 and for indexing it starts from 0
character= "Hello"
print(len(character))

#using loop
name = "Hello"
for i in range(len(name)):
    print(name[i],":",1)


#next question
name1="hello h h h h h a a a a"
count=0
print(len(name1))
for i in range(len(name1)):
    print(name1[i],"",i)
    if name1[i]=="h" or name1[i]=="H":
        count+=1
print("Count of H", count)

#exercise without using loop
name="Hello"
index=0
for x in name:
    print(x, "", index)
    index=index+1
    
    






