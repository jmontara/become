# demonstrate hashtable usage

# create a hashtable all at once

items1 = dict({"key1": 1, "key2" : 2, "key3" : "three"})
print(items1)

# create a hashtable progressively

items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# access a nonexistant key

#print items1["key6"]


# replace an items
items2["key2"] = "two"
print items2

# iterate the keys and values in the dictionary
for key in items2.keys():
	print "key:", key, "value:", items2[key]
	
# iterate the keys and values in the dictionary, sorted by key
for key in sorted(items2.keys()):
	print "key:", key, "value:", items2[key]