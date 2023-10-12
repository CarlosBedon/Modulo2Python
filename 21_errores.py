#print(0/0)
#print(result) Variables que no existen


print('Hola')


suma = lambda x,y : x+y
assert suma(2,2) == 4 #si no cumple la condicion nos envia un AssertionError. Es una verificacion

print ('HOla 2')

try:
    x = 10

    if x<19:
        raise Exception ('Limite de Agua muy bajo')
except Exception as error:
    print (error)