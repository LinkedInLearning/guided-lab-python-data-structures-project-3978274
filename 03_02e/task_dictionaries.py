"""
Python Task Manager App
Storing task data in dictionaries
"""

# Globally available data structures
tasks = [
    {"title": "Watch course introduction video", "status": "complete", "deadline": None},
    {"title": "Fork the course GitHub repository to my own GitHub account", "status": "complete", "deadline": None},
    {"title": "Spin up a GitHub CodeSpace for the forked repository", "status": "pending", "deadline": "2025-10-03"},
    {"title": "Start working through Chapter 2", "status": "pending", "deadline": "2025-10-04"}
]


# Core Functions
def add_task(title, status="pending", deadline=None):
    """Add a new task with status and deadline"""
    global tasks
    task = {"title": title, "status": status, "deadline": deadline}
    tasks.append(task)
    print(f"Task added: {task}")


def delete_task(title):
    """Delete a task by title."""
    global tasks
    task_to_delete = None
    for task in tasks:
        if task["title"] == title:
            task_to_delete = task
            break
    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task deleted: {task_to_delete}")
    else:
        print(f"Task not found: {title}")


def view_tasks():
    """View all tasks."""
    print("\nAll Tasks:")
    if not tasks:
        print("No tasks available.")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['title']} (Status: {task['status']}, Deadline: {task['deadline']})")


# Main Program
if __name__ == "__main__":
    print("Task Manager with Dictionaries")
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
