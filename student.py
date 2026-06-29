students = []
tasks = []

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
        
        sid = len(students) + 1
        
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
        
        tid = len(tasks) + 1
        
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
            if task["student_id"] == search_id:
                print("ID:", task["id"])
                print("Title:", task["title"])
                found_any = True
                
        if not found_any:
            print("No tasks found for this student. .")
            
    elif choice == 4:
        search_id = int(input("Enter the task I D Number: "))
        
        found = False
        for i in range(len(tasks)):
            task = tasks[i]
            if task["id"] == search_id:
                print("ID:", task["id"])
                print("Title:", task["title"])
                print("Description:", task["description"])
                print("Priority:", task["priority"])
                print("Student ID:", task["student_id"])
                print("Status:", task["status"])
                found = True
                
        if not found:
            print("Task is not found.")
            
    elif choice == 5:
        print("displaying Completed Tasks:")
        found_any = False
        for i in range(len(tasks)):
            task = tasks[i]
            if task["status"] == True:
                print("Task ID:", task["id"], "| Title:", task["title"], "| Student:", task["student_id"])
                found_any = True
        if not found_any:
            print("No completed tasks.")
            
    elif choice == 6:
        print("Displaying Pending Tasks:")
        found_any = False
        for i in range(len(tasks)):
            task = tasks[i]
            if task["status"] == False:
                print("Task ID:", task["id"], "| Title:", task["title"], "| Student:", task["student_id"], "| Priority:", task["priority"])
                found_any = True
        if not found_any:
            print("no pending tasks.")
            
    elif choice == 7:
        print("Exiting program.")
        break
        
    else:
        print("Invalid Option")