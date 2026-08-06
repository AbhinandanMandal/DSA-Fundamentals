
# Stack can be implemented via queue
from queue import LifoQueue
stack = LifoQueue(maxsize=3)  # max size is needed to define

# put() to push item into stack
stack.put(1)
stack.put(2)
stack.put(3)

print(stack)
print(type(stack))

print(stack.full())  # returns True if stack is full
print(stack.qsize())  # returns stack size


# get() for pop element
print(stack.get())
print(stack.get())
print(stack.get())
