# Stack Implementation

# Initialize a stack
stack = []
print(stack)  # Output: []

# Append to stack
stack.append(5)
stack.append(6)
stack.append(3)
print(stack)  # Output: [5, 6, 3]

# Pop from stack
x = stack.pop()
print(stack)  # Output: [5, 6]

# Check what is on top of the stack
print(stack[-1])  # Output: 6

# Check if the stack is empty
if not stack:
    print("Empty")
else:
    print("Not Empty")  # Output: Not Empty
