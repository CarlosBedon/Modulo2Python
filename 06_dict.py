
import random


countries = ['col','peru,','ecua','bra']

population_v2 = {country:random.randint(1,100) for country in countries}
print(population_v2)

result = {country:population for (country,population) in population_v2.items() if population > 20 }
print(result)

print(population_v2.items())

texto = 'Hola soy Carlos'
unique = {c:c.upper() for c in texto if c in 'aeiou'}
print(unique)

freq = {c:texto.count(c) for c in texto if c in 'aeiou'}
print(freq)
