# 
# Example file for variables
#

# declare variable and initialize items
f = 0 
print(f)

# re-declaring the variabe works
f = 'abc'
print(f)

# ERROR, variables of different types can not be combined
# python is strongly typed, even though you don't need to declare 
# the value.  The type is inferred by the compiler/interperter.

print("this is a str ", str(1234))


# global vs local variables

f = 0
print(f)

def some_function():
	f = 1
	print(f)
some_function()
	
def some_function():
	global f
	print(f)
some_function()	

# delete variable, should produce a problem	
del f
# print(f)