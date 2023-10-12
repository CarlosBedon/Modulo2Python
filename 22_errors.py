#capturar errores
'''
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

#capturar assert error
try:
    assert 1!=1, "Uno no es igual que uno"
except AssertionError as error:
    print(error)

print("Linea Siguiente")

try:
    x = 10

    if x<19:
        raise Exception ('Limite de Agua muy bajo')
except Exception as error:
    print (error)
'''
#capturar errores
try:
    print(0/0)
    assert 1!=1, "Uno no es igual que uno"
    x = 10
    if x<19:
        raise Exception ('Limite de Agua muy bajo')
except Exception as error:
    print (error)
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)

print("Linea Siguiente")