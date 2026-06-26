courses = { 
    "Java": ["Neeharika","Rohit"],
    "Python": ["Alana","David"],
    "C" : ["Alex","John"]
} #dictionary of courses and students
result={
    student:course for course,students in courses.items() for student in students
} #key=student name value=course ,loop through each course and its list of students ,loop through each student in current course
print(result) #print result dictionary