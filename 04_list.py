
'''
numbers = []
for elements in range(1,11):
    numbers.append(elements * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)
'''

numbers = []
for elements in range(1,11):
    if elements % 2 == 0:
        numbers.append(elements*2)

print(numbers)

numbers_v2 = [element for element in range(1,11) if element % 2 == 0]
print(numbers_v2)