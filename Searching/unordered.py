# search for an item in an unordered list

def find_item(item, itemList):
	# for i in itemList:
		# if i == item:
			# return True
	# return False
	
	# alternative implementation returns position of found item
	for i in range(0, len(itemList)):
		if item == itemList[i]:
			return i
	return None


if __name__ == "__main__":
	item = 1
	itemList = [1, 2, 3, 4]
	print find_item(1, itemList)
	print find_item(2, itemList)
	print find_item(100, itemList)