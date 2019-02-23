# 
# manipulate XML code in memory
#

# see python 3.6.3 documentation, language reference

import xml.dom.minidom

def main():
	# use parse() function to load and parse an XML file\
	doc = xml.dom.minidom.parse("samplexml.xml")
	# print document node and first child name
	# these are standard elements of doc
	print(doc.nodeName)
	print(doc.firstChild.tagName)
	
	# get list of XML tags and /print each
	skills = doc.getElementsByTagName("skill")
	print("%d skills: " % skills.length)
	for skill in skills:
		print ("\t", skill.getAttribute("name"))
	
	# create new tag and add to document
	newSkill = doc.createElement("skill")
	newSkill.setAttribute("name", "serving bales of hay")
	doc.firstChild.appendChild(newSkill)
	
	skills = doc.getElementsByTagName("skill")
	print("%d skills: " % skills.length)
	for skill in skills:
		print ("\t", skill.getAttribute("name"))
		
	
if __name__ == "__main__":
	main();