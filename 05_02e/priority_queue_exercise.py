# Python priority queue using heapq Operations

# Import the heapq module
import heapq

# Create a list of tasks, each with a priority (e.g., 1-5, with 1 as the highest).
# We will store the tasks as tuples with (priority, task).
tasks = [
    (3, "Start working through Chapter 2"),
    (1, "Watch course introduction video"),
    (3, "Fork the course GitHub repository to my own GitHub account")
]

# Create a priority queue by using heapq.heapify() on the tasks list.
heapq.heapify(tasks)

# View the priority queue to see how the tasks are organized by priority
print(tasks)
# Output: [(1, 'Watch course introduction video'), (3, 'Start working through Chapter 2'), (3, 'Fork the course GitHub repository to my own GitHub account')]
# The heap property ensures the smallest priority (1) is at index 0.

# Add a new task to the priority queue with heappush():
heapq.heappush(tasks, (2, "Spin up a GitHub CodeSpace for the forked repository"))

# View the updated priority queue
print(tasks)
# Output: [(1, 'Watch course introduction video'), (2, 'Spin up a GitHub CodeSpace for the forked repository'), (3, 'Fork the course GitHub repository to my own GitHub account'), (3, 'Start working through Chapter 2')]
# The new task with priority 2 is correctly placed.

# Remove the highest priority task (the one with the smallest priority number) using heappop():
highest_priority_task = heapq.heappop(tasks)
print(f"Removed task: {highest_priority_task}")
# Output: Removed task: (1, 'Watch course introduction video')
# The task with priority 1 is removed.

# View the priority queue again after removing the task:
print(tasks)
# Output: [(2, 'Spin up a GitHub CodeSpace for the forked repository'), (3, 'Start working through Chapter 2'), (3, 'Fork the course GitHub repository to my own GitHub account')]
# The next lowest-priority task (2) is now at the root.
