from calendar import c


set_countries = {'mex','col','bra'}

size =len(set_countries)
print(size)


print('col' in set_countries)
print('per' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

#UPDATE
set_countries.update({'ar','ecu','pe'})
print(set_countries)

#remove
set_countries.remove('ar')
print(set_countries)