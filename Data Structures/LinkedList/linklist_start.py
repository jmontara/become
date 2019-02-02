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
		
# the LinkedList class:
class LinkedList(object):
	def __init--(self, head=None):
		self.head = head
		self.count = 0
		
	def get_count(self):
		return self.count
		
	def insert(self, data):
		new_node = Node(data)
		self.count = self.count + 1
	
	def find(self, data):
		#1 get head node
		#2 check for node's match to data
		#3 if match, find is successful, store node 
		#4 if no match, check node fors next
		#5 if next not none, go to 2
		#6 return list of nodess 
			