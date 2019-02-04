# use hash table to filter out duplicates

# define a set of items that we want to eliminate duplicates

items = ["fruit", "fruit", "fruit", "fruit", 
		  "apple", "apple",
		  "orange", "orange",
		  "pear", "pear", "pear"]
		  
# create a hashtable to perform filter
itemsDict = {}

for item in items:
	itemsDict[item] = 0

# populate a list of filtered items
result = []
	
for item in itemsDict.keys():
	result.append(item)

print(items)
print(result)


# populate a set of filtered items 
result = set(itemsDict.keys())
print(result)
	

