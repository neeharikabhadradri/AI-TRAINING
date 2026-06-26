students = [
    {"name" : "Alice", "marks" : 85},
    {"name" : "Bob", "marks" : 90},
    {"name" : "Charlie", "marks" : 78},
    {"name" : "David", "marks" : 92},
    {"name" : "Eve", "marks" : 56}
] # list of student records
def passed_students(records): #generator function
    for student in records:
        if student["marks"] >= 60:
            yield student #yield one passed student at a time

for student in passed_students(students):
    print(student) #print each passed student