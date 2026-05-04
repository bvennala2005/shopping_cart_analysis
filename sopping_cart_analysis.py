
'''shopping cart analysis'''
cart=[
    {"item":"mobile","price":15000,"quantity":1,"category":"electronic"},
    {"item":"pen","price":10,"quantity":2,"category":"stationary"},
    {"item":"boost","price":150,"quantity":1,"category":"gloary"},
    {"item":"mouse","price":2000,"quantity":3,"category":"electronic"},
    {"item":"soap","price":50,"quantity":1,"category":"personalcare"}
]
print(cart)
'''total bill amount'''
def cal_total_bill(cart):
    total=0
    for product in cart:
        total+=product["price"]*product["quantity"]
    return total
print("total_bill:",cal_total_bill(cart))
'''most expensive product'''
def max_cost_of_product(cart):
    max_cost=cart[0]
    for product in cart:
        if product["price"]>max_cost["price"]:
            max_cost=product
    return max_cost
print("maximum cost product is:",max_cost_of_product(cart))
'''min expensive product'''
def cheapest_item(cart):
    cheapest_item=cart[0]
    for product in cart:
        if product["price"]<cheapest_item["price"]:
            cheapest_item=product
    return cheapest_item
print("cheapest item is:",cheapest_item(cart))
'''average price of product'''
def avg_price(cart):
    total_price=0
    for product in cart:
        total_price+=product["price"]
        avg=total_price/len(cart)
    return avg
print("average price of poducts:",avg_price(cart))
'''total quantity of product'''
def total_quantity(cart):
    quantity=0
    for product in cart:
        quantity+=product["quantity"]
    return quantity
print("total quantity of products:",total_quantity(cart))
'''total bill on electronic items'''
def total_bill_elec(cart):
    total=0
    for product in cart:
        if product["category"]=="electronic":
            total+=product["price"]*product["quantity"]
    return total
print("total bill on electronic items:",total_bill_elec(cart))
'''display all products in elctronic category'''
def display_elec_items(cart):
    elec_items=[]
    for product in cart:
        if product["category"]=="electronic":
            elec_items.append(product)
    return elec_items
print("electronic items are:",display_elec_items(cart))