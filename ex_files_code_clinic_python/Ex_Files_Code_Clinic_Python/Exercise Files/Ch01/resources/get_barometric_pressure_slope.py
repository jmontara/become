### code challenge 1
### ask for given start time and end time,
### get barometric pressure from files
### return slope of barometric pressure

import datetime
import csv


def str2datetime(str):
	# print(str)
	yy = str[0:4]
	mo = str[5:7]
	dd = str[8:10]
	hh = str[11:13]
	mm = str[14:16]
	ss = str[17:19]
	yy = int(yy)
	mo = int(mo)
	dd = int(dd)
	hh = int(hh)
	mm = int(mm)
	ss = int(ss)
	# print(yy,mo,dd,hh,mm,ss)
	return datetime.datetime(yy,mo,dd,hh,mm,ss)
	
	
def test_str2datetime():
	""" takes string and returns datetime object"""
	str = '2012_01_01 00:02:14'
	print(str2datetime(str))
# test_str2datetime()

def readfiles():
	""" opens files, returns a list of tuples including datetime and barometric pressure
	"""
	ret = []
	# failed to open the relevant files - fails due to \
	# infile2012 = "C:\Users\john\Documents\GitHub\become\Ex_Files_Code_Clinic_Python\Ex_Files_Code_Clinic_Python\Exercise Files\Ch01\resources\Environmental_Data_Deep_Moor_2012.txt"
	# infile2013 = "C:\Users\john\Documents\GitHub\become\Ex_Files_Code_Clinic_Python\Ex_Files_Code_Clinic_Python\Exercise Files\Ch01\resources\Environmental_Data_Deep_Moor_2013.txt"
	# infile2014 = "C:\Users\john\Documents\GitHub\become\Ex_Files_Code_Clinic_Python\Ex_Files_Code_Clinic_Python\Exercise Files\Ch01\resources\Environmental_Data_Deep_Moor_2014.txt"
	# infile2015 = "C:\Users\john\Documents\GitHub\become\Ex_Files_Code_Clinic_Python\Ex_Files_Code_Clinic_Python\Exercise Files\Ch01\resources\Environmental_Data_Deep_Moor_2015.txt"

	# open the relevant files
	infile2012 = "Environmental_Data_Deep_Moor_2012.txt"
	infile2013 = "Environmental_Data_Deep_Moor_2013.txt"
	infile2014 = "Environmental_Data_Deep_Moor_2014.txt"
	infile2015 = "Environmental_Data_Deep_Moor_2015.txt"
	infiles = [infile2012, infile2013, infile2014, infile2015]
	
	fieldNames = ['datetime', 'Air_Temp', 'Barometric_Press', 'Dew_Point', 'Relative_Humidity', 'Wind_Dir', 'Wind_Gust', 'Wind_Speed']
	
	# with open(infile2012) as tsvfile:
		# reader = csv.DictReader(tsvfile, fieldnames = fieldNames, delimiter='\t')
		# for key in reader.fieldnames:
			# print key

		# maxrows = 3
		# for row in reader:
			# maxrows -= 1
			# print (next(reader))
			# if maxrows < 0:
				# break
		# maxrows = 3
		# for row in reader:
			# maxrows -= 1
			# print('datetime {}, Barometric_Pess {}'.format(row['datetime'],row['Barometric_Press']))
			# if maxrows < 0:
				# break

	for infile in infiles:
		with open(infile) as tsvfile:
			reader = csv.DictReader(tsvfile, fieldnames = fieldNames, delimiter='\t')
			for row in reader:
				try:
					ret.append((str2datetime(row['datetime']),row['Barometric_Press']))
				except:
					print('error appending row, should be a header row:')
					print(row)
	return ret	

def test_readfiles():
	l = readfiles()
	for item in range(10):
		print('head datetime {}, barometric press {}'.format(l[item][0], l[item][1]))
	for item in range(len(l)-10,len(l)):
		print('tail datetime {}, barometric press {}'.format(l[item][0], l[item][1]))
	
def prompt_user():				
	""" Prompts for start and end date time.  Returns start and end datetime objects.
	"""
	
	while True:
		try:
			print ("enter start values for which barometric pressure will be returned:")
			yr = int(input('enter Start Year:'))
			mo = int(input('enter start Month:'))
			day = int(input('enter start Day:'))
			hr = int(input('enter start Hour:'))
			min = int(input('enter start Minute:'))
			sec = int(input('enter start Second:'))
			start = datetime.datetime(yr, mo, day, hr, min, sec)
			
			print ("enter end values for which barometric pressure will be returned:")
			yr = int(input('enter end Year:'))
			mo = int(input('enter end Month:'))
			day = int(input('enter end Day:'))
			hr = int(input('enter end Hour:'))
			min = int(input('enter end Minute:'))
			sec = int(input('enter end Second:'))
			end = datetime.datetime(yr, mo, day, hr, min, sec)
						

			return start, end

		except:
			print ('\n\tnot a valid start or end, try a again')
	
def test_prompt_user():
	print(prompt_user())
	
def main():
	startDateTime,endDateTime = prompt_user()
	print ('/n/tstart, end:', startDateTime, endDateTime)
	l = readfiles()
	lofInterest = []
	for (datetime, Barometric_Pess) in l:
		if datetime >= startDateTime and datetime <= endDateTime:
			lofInterest.append((datetime, Barometric_Pess))
	print lofInterest
	
	
if __name__ == "__main__":
	# test_prompt_user()
	# test_readfiles()	
	main()


