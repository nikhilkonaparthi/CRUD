class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    def __str__(self):
        return f"Task ID: {self.id}, Title: {self.title}, Description: {self.description}"

tasks = []
next_id = 1

def create_task():
    global next_id
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = Task(next_id, title, description)
    tasks.append(new_task)
    next_id += 1
    print("Task created successfully!")

def read_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(task)

def update_task():
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task.id == task_id:
            task.title = input("Enter new task title: ")
            task.description = input("Enter new task description: ")
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found.")

def menu():
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
menu()
