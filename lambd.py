#lambda Function
# square=lambda x: x**2
# print(square(5))

# #Normal function
# def square(num):
#     s=square**2
#     return s
# result=square(5)
# print(result) 

#map
# numbers =[1,2,3,4,5]
# squared= list(map(lambda x: x**2, numbers))
# print(squared)

#filter
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x : x %2==0, numbers))
print(even_numbers)

#reduce ---- we have to import reduce
from functools import reduce
#example1: summing up a list of numbers
numbers=[1,2,3,4,5]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)

#Example2: Finding the maximum numbers in list
numbers=[3,8,1,6,2]
max_num=reduce(lambda x,y: x if x>y else y, numbers)
print(max_num)

#Example3: Concatinating the strings in a list
words=["Hello", "", "world", "!"]
sentence=reduce(lambda x,y: x+y, words)

#Example4: Using an initiator
numbers=[1,2,3,4,5]
product=reduce(lambda x,y: x*y, numbers,1)
print(product)


