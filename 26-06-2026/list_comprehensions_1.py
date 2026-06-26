departments = [
    {"dept": "AI", "employees": ["Neeharika","Rohit"]},
    {"dept": "ML", "employees": ["Alana"]},
    {"dept": "DS", "employees": ["David"]},                             
] #list of dictionaries

result=[emp for dept in departments if dept["dept"]=="AI" for emp in dept["employees"]] #add employee to result list ,loop though each dept dictionary ,process if ai dept,loop ai dept employees
print(result) #print result list