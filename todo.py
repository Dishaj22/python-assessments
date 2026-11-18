
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
