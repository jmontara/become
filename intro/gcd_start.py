# find gcd of two numbers using Euclid's algorithm

def gcd(a,b):
	while (b!=0):
		t = a
		a = b
		b = t % b # gives remainder
		
		
	return a
		
print gcd(20,8)
print gcd(100,10)