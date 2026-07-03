students = []
tasks = []
student_counter = 0
task_counter = 0

while True:
    print("1. Create Student")
    print("2. Add Task")
    print("3. Display all tasks for a student")
    print("4. Display single task")
    print("5. Display Completed Tasks")
    print("6. Display Pending Tasks")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Creating Student Account:")
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        school = input("Enter School: ")
        
        student_counter = student_counter + 1
        sid = student_counter
        
        if sid < 100:
            print("Option: ID has less than 3 characters.")
        
        student = {
            "id": sid, 
            "name": name, 
            "grade": grade, 
            "school": school
        }
        students.append(student)
        print("Success: Created Student with ID", sid)
        
    elif choice == 2:
        print("Adding a Task:")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        priority = input("Enter Priority (low/medium/high): ")
        student_id = int(input("Enter Student ID Number: "))
        
        task_counter = task_counter + 1
        tid = task_counter
        
        if tid < 100:
            print("Option: ID has less than 3 characters.")
        
        task = {
            "id": tid, 
            "title": title, 
            "description": description, 
            "priority": priority, 
            "student_id": student_id, 
            "status": False
        }
        tasks.append(task)
        print("Success: Added Task with ID", tid)
        
    elif choice == 3:
        search_id = int(input("Enter the student ID Number: "))
        print("Tasks")
        
        found_any = False
        for i in range(len(tasks)):
            task = tasks[i]
            if task["student_id"] == search_
