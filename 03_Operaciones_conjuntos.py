from re import S


set_a = {'col','mex','bol'}
set_b = {'pe','bol'}
#union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)
#intrseccion
set_c = set_a.intersection(set_b)   
print(set_c)
print(set_a & set_b)
#DIFERENCIA
set_c = set_a.difference(set_b)   
print(set_c)
print(set_a - set_b)

#diferencia simetrica
set_C = set_a.symmetric_difference(set_b)   
print(set_c)
print(set_a ^ set_b)
