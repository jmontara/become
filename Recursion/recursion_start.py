# recursive implementations of power and functions


def power(num,pwr):
	""" gives number to the power 
	
	inputs:
		num - int, number
		pwr - int, power
	
	outputs:
		ret - int, number to the power
	"""
	if pwr == 0:
		return 1
	else:
		return num * power(num, pwr - 1)

def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)
		
num = 3
pwr = 3
print num, "to the power of ", pwr, " = ", power(num,pwr)
print num, "factorial = ", factorial(num)

num = 4
print num, "to the power of ", pwr, " = ", power(num,pwr)
print num, "factorial = ", factorial(num)

num = 0
print num, "to the power of ", pwr, " = ", power(num,pwr)
print num, "factorial = ", factorial(num)