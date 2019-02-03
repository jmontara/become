# try out the Python stack functions

# create a new empty stack
class Stack(object):
	def __init__(self):
		self.Stack = []
		

# push items onto the stack
	def push(self, item):
		self.Stack.append(item)

# print the stack contents
	def print_stack(self):
		for item in self.Stack:
			print "item in stack:", item

# pop an item off the stack
	def pop(self):
		return self.Stack.pop()
		
def testStack():
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.print_stack()
	x = s.pop()
	print "pop item value:", x
	print "stack after pop():"
	s.print_stack()
	
testStack()
