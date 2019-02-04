# bubble sort algorithm

def bubble_sort(dataset):
	""" mutates dataset into sorted order"""
	# start with array length and decrement each time 
	arrayLen = len(dataset)
	bubbleIndex = len(dataset) - 1
	while bubbleIndex != 0:
		arrayIndex = 0
		while arrayIndex < arrayLen - 1:
			thisVal = dataset[arrayIndex]
			nextVal = dataset[arrayIndex + 1]
			if thisVal > nextVal:
				dataset[arrayIndex + 1] = thisVal
				dataset[arrayIndex] = nextVal
			arrayIndex += 1
		print "Current State:", dataset
		bubbleIndex -= 1
		

		
		

		
	
def main():
	list1 = [ 6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
	print "list: ", list1
	bubble_sort(list1)
	print "bubble sorted list: ", list1
	

if __name__ == "__main__":
	main()
	