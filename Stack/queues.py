# Queue Implementation using deque
from collections import deque

# Initialize a queue
q = deque()
print(q)  # Output: deque([])

# Enqueue - Add elements to the right (O(1))
q.append(5)
q.append(6)
q.append(7)
print(q)  # Output: deque([5, 6, 7])

# Dequeue - Remove elements from the left (O(1))
q.popleft()
print(q)  # Output: deque([6, 7])

# Peek from the left side (O(1)) and peek from the right side (O(1))
print(q[0])  # Peek from the left: Output: 6
print(q[-1])  # Peek from the right: Output: 7

