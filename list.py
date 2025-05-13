#lists are data types. They are mutable/changeable ---- creating list of numbers, string and mixed list
numbers=[1,2,3,4,5]
fruits=["apple", "banana", "cherry"]
mixed_list=[10, "Hhello", True, 3.14]

#to print use the logic of indexing
print(numbers[0])
print(fruits[1])
print(mixed_list[2])

#Using range to print
fruits=["apple", "banana", "cherry"]

for x in range(len(fruits)):
    print(fruits[x])

#next question-- print a and A in the list
mixed=["apple", "fruits", 1,2, "dog",3, True,"gun", "Ant"]
for x in mixed:
    print(type(x))
    if type(x)==str and "a" in str(mixed).lower():
     print(mixed)

#question
mix=["apple","apple",1,2,"dog",3,True,"gun","apple"]
for index in range(len(mix)):
    print(index)
    if mix[index] == "apple":
        mix[index] = "banana"

print(mix)




