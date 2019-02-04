# use recursion to count down

def countdown(fromnumber):

	print(fromnumber)
	if fromnumber == 0:
		print "complete!"
		return
	else:
		countdown(fromnumber -1)
		print "foo"
		
countdown(4)