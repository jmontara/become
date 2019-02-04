# use hash table to count number of unique items in set

# define a set of items that we want to eliminate duplicates
items = ["fruit", "fruit", "fruit", "fruit", 
		  "apple", "apple",
		  "orange", "orange",
		  "pear", "pear", "pear"]
		  
# create a hashtable to perform filter and store counts
itemsDict = {}

for item in items:
	
	itemsDict[item] = itemsDict.get(item,0) + 1

# populate a list of filtered items
result = []
for item in itemsDict.keys():
	result.append((item, itemsDict[item]))

print("items:", items)
print("result:", result)

# populate a set of filtered items 
# result = set(itemsDict.keys())

# print(result)
	

