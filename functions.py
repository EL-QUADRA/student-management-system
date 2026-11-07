students = [
    {"name": "Kidus", "GPA": 3.99},
    {"name": "Abel", "GPA": 2.85},
    {"name": "Dawit", "GPA": 3.45},
    {"name": "Henok", "GPA": 2.45},
    {"name": "Miki", "GPA": 3.75}
]
def print_students(students):
    for student in students:
        print(student["name"])

print_students(students)

def count_low_gpa(students):
    count = 0
    for student in students:
        if student["GPA"] < 3.0:
            count +=1
    return count
print(count_low_gpa(students))

def calculate_average(students):
    total_gpa = 0
    for student in students:
        total_gpa += student["GPA"]
    average_gpa = total_gpa / len(students)
    return average_gpa
print(calculate_average(students))
