# try out the python queue functions

from collections import deque

# create a new empty queue
queue = deque()

# add some elements
queue.append(1)
queue.append(2)
queue.append(3)

print queue

# pop an item from the right

x = queue.popleft()

print(x)
print(queue)
