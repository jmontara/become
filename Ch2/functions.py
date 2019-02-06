#
# example file for working with functions
#

def func1():
	print("This is a function")
	
	
	
def func2(arg1, arg2):
		print (arg1, " ", arg2)
		
		
	
	
	
def power(num, pwr):
	ret = num
	for x in range(pwr-1):
		ret = ret * num
	return ret
	
	
	
def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	
	return result
	
	
	
	
	
# func1()
# print(func1())
# print (func1)

# func2(10,20)
# print (func2(10,20))

print (power(pwr=3, num=3))

print (multi_add(4,5,10,20))
