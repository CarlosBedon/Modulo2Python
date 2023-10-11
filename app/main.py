import mod

keys, values = mod.get_popullation()
print (keys,values)


data = [
    {
        'Country':'Colombia',
        "Population":500
    },
    {
        'Country':'Ecuador',
        "Population":200
    }
]

result = mod.popullation_by_country(data,'Ecuador')
print(result)