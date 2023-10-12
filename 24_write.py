'''
with open('./texto.txt','r+') as file:
    for line in file:
        print(line)
    file.write('Se utiliza para escribir nuevas cosas\n')
    file.write('nueva linea\n')
    file.write('segunda linea\n')
    print('Anterior')
'''
#SOBRE ESCRIBE TODO EL ARCHIVO
with open('./texto.txt','w+') as file:
    for line in file:
        print(line)
    file.write('Se utiliza para escribir nuevas cosas\n')
    file.write('nueva linea\n')
    file.write('segunda linea\n')
    print('Anterior')  
    
