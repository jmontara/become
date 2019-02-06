
# predeifined in python library 
from datetime import date
from datetime import time
from datetime import datetime


def main():
	# today = date.today()
	# print ("Today's date is ", today)
	
	# print ("Date components: ", today.day, today.month, today.year)
	# print ("today's weekday number is:", today.weekday())
	# days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
	# print ("which is a :", days[today.weekday()])

	today = datetime.now()
	print ("the current datetime is: ", today)
	t = datetime.time(datetime.now())
	print ("the current time is: ", t)
if __name__ == "__main__":
	main()