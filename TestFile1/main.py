students = [
    {"Name" : 'Alice', 
     "Letter" : 'B', 
     "Age": 18},
     {"Name" : 'Alice', 
     "Letter" : 'B', 
     "Age": 17},
     {"Name" : 'Alice', 
     "Letter" : 'B', 
     "Age": 19}
]

# Sort by age (second element of each tuple)
sorted_by_age = sorted(students, key=lambda student: student["Age"])
print(sorted_by_age)