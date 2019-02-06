

def main():
	x = 0
	
	while (x<5):
		print(x)
		x += 1
		
		
	for x in range(5,10):
		print(x)
		

	months=["jan", "feb", "mar"]
	for m in months:
		print(m)
		
	for x in range(5,10):
		if x == 7:  break
		print(x)
		
	for x in range(5,10):
		if x == 7:  continue
		print(x)
		
	for x in range(5,10):
		if x%2 == 0:  continue
		print(x)	
		
	months=["jan", "feb", "mar"]
	for i,m in enumerate(months):
		print(i,m)
		
			
		
if __name__ == "__main__":
	main()