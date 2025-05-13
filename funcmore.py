#creating empty list and putting the value in empty list
def abc(number):
    final=[]
    maximum=max(number)
    minimum=min(number)
    total_sum=sum(number)
    final.append(maximum)
    final.append(minimum)
    final.append(total_sum)
    return final
number=[1,2,3,4]
results=abc(number)
print(results)
maximum=results[0]
minimum=results[1]
sum=results[2]
print("maximun value:",maximum)
print("minimum value:",minimum)
print("sum value:",sum)

#printing in dictionary
value=abc(number)
print(("max",value[maximum]))
print(("min",value[minimum]))
print(("sum",value[sum]))



