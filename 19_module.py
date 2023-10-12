
import sys 
print(sys.path) #ruta en la maquina que estoy ejecutando el archivo

import re #utilizado para expresiones regulares busqueda mas inteligente
text = 'Mi numero de telefono 311 123 121, el codigo del pais es 57, mi numero de la suerte es el 13'
result= re.findall('[0-9]+',text)
print (result)

import time #hora fecha
timestamp = time.time()
print(timestamp)

local = time.localtime()
result=time.asctime(local)
print(result)

import collections #utilidad para manejar listas
numbers=[1,1,12,1,2,1,2,4,5,3,3,2]

counter = collections.Counter(numbers)
print(counter)