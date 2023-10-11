price = 1000 #price es variable global alcance global

def increment(price = 0): #price  es variable local dentro de la funcion
    price  = price + 10 
    print(price)

print(price)

increment()