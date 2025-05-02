import heapq

tasks = [
    {"title": "Task A", "status": "complete", "deadline": None, "priority": 5},
    {"title": "Task B", "status": "complete", "deadline": None, "priority": 5},
    {"title": "Task C", "status": "pending", "deadline": "2025-10-03", "priority": 1},
    {"title": "Task D", "status": "pending", "deadline": "2025-10-04", "priority": 2}
]

# Priority queue (using heapq)
priority_queue = [(task["priority"], idx, task) for idx, task in enumerate(tasks)]
heapq.heapify(priority_queue)

print(priority_queue)