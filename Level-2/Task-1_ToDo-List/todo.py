import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except IndexError:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['task']}")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\n1.Add  2.View  3.Mark Done  4.Delete  5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task(input("Enter task: "))
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        mark_done(int(input("Task number: ")) - 1)
    elif choice == "4":
        view_tasks()
        delete_task(int(input("Task number: ")) - 1)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
