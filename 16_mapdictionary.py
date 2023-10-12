
items=[
 {
    'producto':'camisa',
    'price':100
 },
 {
    'producto':'pantalones',
    'price':300
 },
 {
    'producto':'jeans',
    'price':200
 },
]

#print(items)

prices=list(map(lambda item:item['price'],items))
print (prices)

def add_taxes(item):
    item['taxes']= item['price']*.12
    return item

#new_items = list(map(add_taxes,items ))
#print(new_items)

