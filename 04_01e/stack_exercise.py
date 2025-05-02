# Basic Stack Operations

# Create an empty stack
stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)  # Output: [10, 20, 30]

# Pop an element from the stack (removes the last element)
print(stack.pop())  # Output: 30
print(stack)  # Output: [10, 20]

# Peek at the top element without removing it
print(stack[-1])  # Output: 20
print(stack)  # Output: [10, 20] (unchanged)

# Check if the stack is empty
if not stack:  # Equivalent to if len(stack) == 0
    print("Stack is empty")
else:
    print("Stack is not empty")  # Output: Stack is not empty

# Use a stack to reverse a list by popping all elements
stack = [1, 2, 3, 4, 5]
reversed_list = []

while stack: # Equivalent to `while len(stack) > 0`
    reversed_list.append(stack.pop())

print(reversed_list)  # Output: [5, 4, 3, 2, 1]
