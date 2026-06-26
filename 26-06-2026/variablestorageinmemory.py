import os
import sys
x=10 #create an int variable
print("The value of x is:",x) #print value stored in x
print("The memory address/object ID of x is:",id(x))  #print memory address/location of x
print("The type of x is:",type(x)) #show datatype of x
print("The size of x is:",sys.getsizeof(x) ,"bytes") #show size memory of x in bytes
print("The process ID of the current process is:",os.getpid()) #process ID assigned by OS