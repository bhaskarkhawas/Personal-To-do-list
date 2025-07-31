import json
import os

# Define the Task class to represent a to-do item
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# File to store the tasks
TASKS_FILE = "tasks.json"

# Save the list of tasks to a JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        data = json.load(f)
        return [Task(**task_data) for task_data in data]

# Add a new task to the list
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter category (e.g., Work, Personal, Urgent): ")
    new_task = Task(title, description, category)
    tasks.append(new_task)
    print("Task added successfully.\n")

# View all tasks with their details
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.\n")
        return
    for idx, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx + 1}. {task.title} [{status}]")
        print(f"   Description: {task.description}")
        print(f"   Category: {task.category}\n")

# Mark a specific task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num].mark_completed()
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Delete a task from the list
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted = tasks.pop(task_num)
            print(f"Deleted task: {deleted.title}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main menu-driven function
def main():
    tasks = load_tasks()
    while True:
        print("To-Do List Application Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
