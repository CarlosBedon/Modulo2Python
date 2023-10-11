'''
Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.

La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

Ejemplo 1:

Input: ['amor', 'sol', 'piedra', 'día']
Output: [ 'amor', 'piedra' ]

Ejemplo 2:

Input: ['rosa', 'gol', 'pez', 'día', 'gafas']
Output: [ 'rosa', 'gafas' ]

'''

def filter_by_length(words):
   letras = list(filter(lambda text:len(text) >= 4,words))
   return letras




words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)