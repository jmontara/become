# searching an ordered list

# get index of first, last items, and mid 
# if value of mid is equal to searched for value, then done
# if value of mid point is greater than, then 
#  recursively call with midpoint being new first
# else 
#  recursively call with midpoint being last


def find_ordered(findItem, orderedItems):

	listSize = len(orderedItems) - 1

	lowerIndex = 0
	upperIndex = listSize
	
	while lowerIndex <= upperIndex:
		
		middleIndex = (upperIndex + lowerIndex)//2
		
		if orderedItems[middleIndex] == findItem:
			return middleIndex
			
		else:
			if orderedItems[middleIndex] < findItem:
				lowerIndex = middleIndex + 1
			else:
				upperIndex = middleIndex - 1
			
		
		
if __name__ == "__main__":
	orderedItems = [1, 2, 3, 4, 55, 66, 77, 88, 99]
	print find_ordered(0,orderedItems)
	print find_ordered(3,orderedItems)
	print find_ordered(100,orderedItems)
	
	
	

	

