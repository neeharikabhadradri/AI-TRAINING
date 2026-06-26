orders=[
    {"id": 101, "customer": "Jack", "amount": 2500},
    {"id": 102, "customer": "Jill", "amount": 1500},
    {"id": 103, "customer": "John", "amount": 300},
    {"id": 104, "customer": "Jane", "amount": 1000},
] # list of customer orders
def process_orders(data):    #generator function 
    for order in data:
        if order["amount"] > 1000:   #if order amount is greater than 1000, calculate discount and final amount
            discount =order["amount"] * 0.1
            final_amount= order["amount"] - discount
            yield {    #yield processed order one at a time 
                "Order ID": order["id"],
                "Customer": order["customer"],
                "Original Amount": order["amount"],
                "Discount": discount,
                "Final Amount": final_amount
            }
for order in process_orders(orders):
    print(order)  #print each processed order

