# Basic Operations with Python collections.deque

# Import deque
from collections import deque

# Initialize an empty queue
queue = deque()

# Add elements (enqueue)
queue.append("Task A")
queue.append("Task B")
queue.append("Task C")

# Check queue state
print(queue)  # Output: deque(['Task A', 'Task B', 'Task C'])

# Remove elements from the front
print(queue.popleft())  # Output: Task A
print(queue.popleft())  # Output: Task B
print(queue)  # Output: deque(['Task C'])

# Check if a Queue is Empty
if not queue:  # equivalent to if len(queue) == 0
    print("Queue is empty")
else:
    print("Queue is not empty")  # Output: Queue is not empty

# Peek at the first element without removing it
print(queue[0])  # Output: Task C
