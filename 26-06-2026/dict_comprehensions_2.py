products=[
    {"id":"201","name":"Laptop","price":80000,"stock":True,"category":"Electronics"},
    {"id":"202","name":"Smartphone","price":50000,"stock":False,"category":"Electronics"},
    {"id":"203","name":"Headphones","price":2000,"stock":True,"category":"Electronics"},
    {"id":"204","name":"Shoes","price":3000,"stock":True,"category":"Fashion"},
    {"id":"205","name":"T-shirt","price":1000,"stock":False,"category":"Fashion"}
] #list of dictionaries
result={product["name"]:product["price"] for product in products if product["stock"] and product["price"]>1000} #key=product name and value=product price ,loop through products in list,keep the products that are in stock and above 1000 
print(result) #print result dictionary