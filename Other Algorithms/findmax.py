# recursive algorithm to find a maximum value


# list of values to operate on
items = [ 10, 9, 8, 100, 20, 29, 47, 98]

def find_max(items):
	""" takes list of numeric values
	    returns max numeric value"""

	# # breaking condition, last item in list, return item
	# if len(items) == 1:
		# return items[0]
	
	# # compare first item in list to second, return item with greatest value
	# # start a chain of function calls
	# val0 = items[0]
	# val1 = find_max(items[1:])
	
	# if val0 > val1:
		# return val0
	# else:
		# return val1
		
		
	# alternative implementation with print statements shows what's going on	
	
	
	# breaking condition, last item in list, return item
	if len(items) == 1:
		return items[0]
	
	# compare first item in list to second, return item with greatest value
	# start a chain of function calls
	val0 = items[0]
	print ("val0:", val0)
	val1 = find_max(items[1:])
	print("val1:", val1)
	
	if val0 > val1:
		return val0
	else:
		return val1
		

print(items)		
print(find_max(items))