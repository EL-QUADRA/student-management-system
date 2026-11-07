print("====================================")
print("University student management system")
print("====================================")

students = [
    {"name": "kidus", "result": 400, "id": 101},
    {"name": "yabsira", "result": 371, "id": 102}
]
def register():
    stud_name = input("Enter your name: ")
    stud_result = int(input("Enter your entrance exam result: "))
    if stud_result < 300:
        print("you did not qualify to join university")
        return

    IDs = []
    for stud in students:
        IDs.append(stud["id"])
    last_id = max(IDs)

    student = {
        "name": stud_name,
        "result": stud_result,
        "id": last_id + 1
    }
    students.append(student)
    
def view_all():
    for people in students:
        print(people)

def search_student():
    key = int(input("Enter ID number to search: "))
    for student in students:
        if key == student["id"]:
            return student
    
    print("student not found")

def update_student():
    print("NOTE: ID NUMBER OF A STUDENT IS IMMUTABLE")
    mod_student = search_student()
    print("Enter new attributes to update: ")
    new_name = input("new name: ")
    new_result = int(input("Enter new entrance result: "))
    mod_student["name"] = new_name
    mod_student["result"] = new_result
    return mod_student

def delete_student():
    key = int(input("Enter student ID to remove: "))
    for student in students:
        if key == student["id"]:
            students.remove(student)
            print("student successfully deleted!!!")
            print(students)
            return students
        
    print("student not found")
    return

def academic_analytics():
    results = []
    count = 0
    for student in students:
        count += 1
        results.append(student["result"])
        total = sum(results)

    average_score = total / count
    max_score = max(results)
    min_score = min(results)
    print("Highest result: ", max_score)
    print("Lowest result: ", min_score)
    print("Total students: ", count)
    print("Average score: ", average_score)

#for this example we will use students who scored over 450
def filter_students():
    counter = 0
    for stud in students:
        if stud["result"] >= 450:
            counter += 1
            print(stud)
        else:
            continue
    if counter == 0:
        print("No student meets the requirement!")
                
while True:
    print("1. Register")
    print("2. view all students")
    print("3. search student")
    print("4. update a student")
    print("5. delete student")
    print("6. Academic alanytics")
    print("7. filter students")
    print("8. exit")
    choice = int(input(":-"))
    if choice == 1:
        register()
    elif choice == 2:
        view_all()
    elif choice == 3:
        print(search_student())
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        academic_analytics()
    elif choice == 7:
        filter_students()
    elif choice == 8:
        quit()
    else:
        print("invalid choice!")
        continue