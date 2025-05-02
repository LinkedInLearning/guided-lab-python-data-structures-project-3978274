"""
Python Task Manager App
Storing tasks as strings within a list
"""

# Globally available data structure
tasks = [
    "Watch course introduction video",
    "Fork the course GitHub repository to my own GitHub account",
    "Spin up a GitHub CodeSpace for the forked repository",
    "Start working through Chapter 2"
]


# Core Functions
def add_task(task):
    """Add a new task"""
    global tasks
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(task):
    """Delete a task by its name."""
    global tasks
    if task in tasks:
        tasks.remove(task)
        print(f"Task deleted: {task}")
    else:
        print(f"Task not found: {task}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Lists")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View All Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            title = input("Enter task title: ")
            status = input("Enter task status (default: pending): ") or "pending"
            deadline = input("Enter task deadline (optional): ") or None
            add_task(title, status, deadline)
        elif choice == "2":
            title = input("Enter task title to delete: ")
            delete_task(title)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
