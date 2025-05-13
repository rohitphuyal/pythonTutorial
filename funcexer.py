def stats(num):
    max1=max(num)
    min1=min(num)
    sum1=sum(num)
    return max1,min1,sum1
number=[1,2,3,4,5]
result=stats(number)
print(result)
print(type(result))
maximum=result[0]
minimum=result[1]
sum=result[2]
print("maximun value:",maximum)
print("minimum value:",minimum)
print("sum value:",sum)
