
# Also stack can be implemented with deque module from collections
# Basic utilization of deque is, it's efficient in insertion and deletion in O(1) of time

from collections import deque
stack = deque()

# for insertion we similarly use append()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
print(type(stack))


print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
