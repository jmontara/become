# determine if a list is sorted

def is_sorted(list):
	""" returns true if sorted in ascending order, false if not"""
	
	# alternative implementation #1
	# for i in range(0, len(list) - 1):
		# if list[i] > list[i+1]:
			# return False
	# return True
	
	
	
	#  alternative implementation #2
	# for i in range(0, len(list) - 1):
		# if list[i] <= list[i+1]:
			# i += 1
			# continue
		# else:
			# return False
	# return True
	
	
	return all(list[i] <= list[i+1] for i in range(0, len(list)-1))
	

if __name__ == "__main__":
	list = [0, 1, 2, 3, 4]
	print list, "is_sorted(list) gives: ", is_sorted(list)
	list.append(-1)
	print list, "is_sorted(list) gives: ", is_sorted(list)
	
		