# Linked list example

# the Node class
class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None
	
	def get_data(self):
		return self.val
	
	def set_data(self, val):
		self.val = val
		
	def get_next(self): 
		return self.next
	
	def set_next(self, next):
		self.next = next

def testNodeObject():
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	print "testNodeObject() gives: "
	print "n1, n2, n3:", n1, n2, n3
	d1 = n1.get_data()
	d2 = n2.get_data()
	d3 = n3.get_data()
	print "d1, d2, d3:", d1, d2, d3
	n1.set_next(n2)
	n2.set_next(n3)
	n1Next = n1.get_next()
	n2Next = n2.get_next()
	n3Next = n3.get_next()
	print "n1Next, n2Next, n3Next:", n1Next, n2Next, n3Next		

testNodeObject()		
				
		
# the LinkedList class:
class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
		self.count = 0
		
	def get_count(self):
		return self.count
		
	def insert(self, data):
		# Insert a new node; for sake of simplicity, insert only at the head.
		new_node = Node(data)
		# set head to current head of list
		new_node.set_next(self.head)
		# tell head to point to the new head
		self.head = new_node
		self.count += 1
		
	def find(self, data):
		# find and return the first node with a given value
		n = self.head
		while (n != None):
			if n.get_data() == data:
				return n
			else:
				n = n.get_next()
		return 
		
	def dump_list(self):
		n = self.head
		while n != None:
			print "node: ", n.get_data()
			n = n.get_next()

	def deleteAt(self, index):
		# delete node at given index
		# check if node is within the number of existing nodes in the list
		if index > self.count -1:
			return
		if index == 0:
			self.head = self.head.get_next()
			self.count -= 1
		else:
			tmpIndex = 0
			node = self.head
			while tmpIndex < index -1:
				node = node.get_next()
				tmpIndex  += 1
			node.set_next(node.get_next().get_next())
			self.count -= 1
				
		
def testLinkedListObject():
	ll = LinkedList()
	ll.insert(1)
	ll.insert(10)
	ll.insert(100)
	ll.insert(1000)

	print "\ntestLinkedListObject() gives:"
	print "ll.dump_list() gives: \n", ll.dump_list()
	print "ll.find(1) gives: ", ll.find(1)
	print "ll.find(2) gives: ", ll.find(2)
	print "delete an item gives: \n"
	print "before delete:"
	print "ll.get_count():", ll.get_count()
	ll.dump_list()
	ll.deleteAt(3)
	print "after delete:"
	print "ll.get_count()", ll.get_count()
	ll.dump_list()
	
			
testLinkedListObject()

		
		
		
		
		
		
		
		
		
			