
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
    new_item = item.copy()
    new_item['taxes']= new_item['price']*.12
    return new_item

new_items = list(map(add_taxes,items ))
print('New List')
print(new_items)
print("Old List")
print (items)
