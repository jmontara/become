#
# parsing and processing HTML
#

from html.parser import HTMLParser



metacount = 0;  # global var

class MyHTMLParser(HTMLParser):
	def handle_comment(self, data):
		print("Encountered comment: ", data)
		pos = self.getpos()
		print ("\tAt line:", pos[0], " position ", pos[1])
	
	def handle_starttag(self,tag, attrs):
		global metacount
		if tag == 'meta':
			metacount += 1
		print("Encountered start tag: ", tag)
		pos = self.getpos()
		print ("\tAt line:", pos[0], " position ", pos[1])
		
		if attrs.__len__() > 0:
			print ("\tAttributes: ")
			for a in attrs:
				print ("\t", a[0], "=", a[1])
	
	def handle_endtag(self, tag):
		print("Encountered end tag: ", tag)
		pos = self.getpos()
		print ("\tAt line: ", pos[0], "position", pos[1])
	
	def handle_data(self, data):
		if (data.isspace()):
			return
		print("Encountered data: ", data)
		pos = self.getpos()
		print ("\tAt line:", pos[0], " position ", pos[1])
	
def main():
	# instantiate parser and feed it some HTML
	parser = MyHTMLParser()
	f = open("something.html")
	if f.mode == 'r':
		contents = f.read()
		parser.feed(contents)
	global metacount
	print("Meta tags counted:", metacount)
		
	## failed implementation from website throws error
	## parser can not read binary 
	# import urllib.request	
	# webUrl = urllib.request.urlopen("https://victoryhillfarm.net/contact-us/")
	# print("result code: " , str(webUrl.getcode()))	
	# if webUrl.getcode() == 200:
		# contents = webUrl.read()
		# print(contents)
		# parser.feed(contents)	
	
if __name__ == "__main__":
	main()
	
