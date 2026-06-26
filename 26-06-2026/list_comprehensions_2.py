patients=[
    {"id":"101","name":"John","age":30,"disease":"Flu"},
    {"id":"102","name":"Neeharika","age":25,"disease":"Cold"},
    {"id":"103","name":"Bob","age":40,"disease":"Diabetes"},
    {"id":"104","name":"Charlie","age":35,"disease":"Hypertension"},
    {"id":"105","name":"Diana","age":28,"disease":"Asthma"}
] #list of dictionaries 
result=[patient["name"] for patient in patients if patient["age"]>30] #add patient name to result list ,loop through each patient dictionary ,process if age>30
print(result) #print result list