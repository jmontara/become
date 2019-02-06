
import os
from os import path
import shutil
from shutil import make_archive # zip
from zipfile import ZipFile     # zip with file selection

def main():
	
	if path.exists("textfile.txt"):
		
		src = path.realpath("textfile.txt")
		dest = src + ".bak"

		shutil.copy(src, dest)

		shutil.copystat(src, dest)
		
		# rename the original file
		# os.rename("textfile.txt", "newfile.txt")
		# os.rename("newfile.txt", "textfile.txt")
		
		# put things into a ZIP archive
		root_dir, tail = path.split(src)
		# print(str(root_dir))
		shutil.make_archive("archive", "zip", root_dir)
		
		# with allows creation of new scope for working with object
		with ZipFile("testzip.zip", "w") as newzip:
			# put just a couple of files into the zip file
			newzip.write("textfile.txt")
			newzip.write("textfile.txt.bak")
		
if __name__ == "__main__":
	main()