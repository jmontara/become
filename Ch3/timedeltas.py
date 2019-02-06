

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print items

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("today is: ", now)

td = timedelta(days=365)
print("one year from now will be: ", str(now + td))


print("in two days and three weeks it will be " +
	  str(now + timedelta(days=2, weeks=3)))