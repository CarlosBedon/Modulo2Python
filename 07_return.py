def sum_with_range(min,max):
    print(min,max)
    sum=0
    for x in range(min,max):
        sum += x
    return sum

result = sum_with_range(1,10)
print('--->', result)
sum_with_range(10,1)
print('--->')
sum_with_range(20,30)

