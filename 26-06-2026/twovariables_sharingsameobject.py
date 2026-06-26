import sys
a=100 #create an int variable
b=a #b stores a refernce to the same object as a
print("The value of a is:",a) #print value stored in a
print("The value of b is:",b) #print value stored in b
print("The ID of a is:",id(a)) #print memory address of a and b
print("The ID of b is:",id(b))

print("Memory of object : ",sys.getsizeof(a),"bytes") #print size of memory of object a and b