import os
from string import *
import sys

folderName = ""
dist = "" 
scope = ""

class Snippet:
	def __init__(self, name="0", key="0", snippet="0"):
		self.name = name
		self.key = key
		self.snippet = snippet

	def _checkSnippetSucces(self):
		if (self.name == "0") or (self.key != "0") or (self.snippet != "0"):
			return True
		else:
			return False

	def create_snippet(self):
		if self._checkSnippetSucces:
			snippetFile = open(dist + '/' + self.key + '.sublime-snippet', 'w')
			snippetFile.write(
			'''
<snippet>
	<content><![CDATA[
{}
]]>
</content>
	<tabTrigger>{}</tabTrigger>
	<description>{}</description>
	<scope>{}</scope>
</snippet>
			'''.format(self.snippet, self.key, self.name, scope)
			)
			snippetFile.close()
		else:
			print "Error in {}".format(self)

	def __str__(self):
		return "Name: {}\nKey: {}\nSnippet {}".format(
			self.name, self.key, self.snippet)
	

def create_snippets():
	mas = os.listdir(folderName)
	mas = [i for i in mas if not i.startswith('.')]
	print 'find {} snippets'.format(len(mas))

	if dist in os.listdir('.'):
		pass
	else:
		os.mkdir(dist)
	for i in mas:
		snip = open(folderName + "/" + i, 'r')
		snp = Snippet()
		checker = False
		for line in snip:
			if checker:
				snp.snippet += line
			if find(line, "# name:") != -1:
				name = line[find(line, "# name:") + len("# name:"):].strip()
				snp.name = name
			if find(line, "# key:") != -1:
				key = line[find(line, "# key:") + len("# key:"):].strip()
				snp.key = key
			if find(line, "# --") != -1:
				checker = True
				snp.snippet = ''
				continue
		snp.create_snippet()
		snip.close()
	print "DONE"

arg = sys.argv
if len(arg) == 4:
	folderName = arg[1]
	dist = arg[2]
	scope = arg[3]
	create_snippets()
else:
	print arg
	print "error arguments"
	print "please use\npython main.py snippet_folder dist_folder sublime_scope_snippet"


