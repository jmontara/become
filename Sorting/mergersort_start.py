# implement merge sort with recursion


def mergesort(dataset):
	""" mutates dataset to a sorted dataset; sorts in place """
	if len(dataset) > 1:                      # breaking point when recursion stops
		mid = len(dataset) // 2
		leftarr = dataset[:mid]
		rightarr = dataset[mid:]
		
		# recursively break down arrays
		mergesort(leftarr)
		mergesort(rightarr)
		
		# merge
		i = 0 # left array index
		j = 0 # index into the right array
		k = 0 # index into merged array
		
		# while both of the sorted arrays still have content
		while i < len(leftarr) and j < len(rightarr):
			# 
			if leftarr[i] < rightarr[j]:
				dataset[k] = leftarr[i]
				i += 1
			else:
				dataset[k] = rightarr[j]
				j += 1
			k += 1
			# print "left", leftarr, "right:", rightarr, "dataset:", dataset
		# if left array has values, add them
		while i < len(leftarr):
			dataset[k] = leftarr[i]
			i += 1
			k += 1
		while j < len(rightarr):
			dataset[k] = rightarr[j]
			j += 1
			k += 1
			
def test_mergesort():

	items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53, 102]

	print "items before sort: ", items
	mergesort(items)
	print "items after sort: ", items
		
test_mergesort()
		