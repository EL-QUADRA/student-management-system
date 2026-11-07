students = [
    {"name": "Kidus", "GPA": 3.99},
    {"name": "Abel", "GPA": 2.85},
    {"name": "Dawit", "GPA": 3.45},
    {"name": "Henok", "GPA": 2.45},
    {"name": "Miki", "GPA": 3.75}
]
for someone in students:
    if(someone["GPA"] < 3.5):
        continue
    print(someone["name"])

count = 0
sum = 0
for people in students:
    if(people["GPA"] < 3.0):
        count += 1
    sum += people["GPA"]
    average = sum / len(students)
print("There are ", count, " people with less than 3.0 GPA")
print("The average GPA is", average)

