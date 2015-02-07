import sublime
import sublime_plugin
import re

class LessThanParseCommand(sublime_plugin.TextCommand):
	def run(self, edit):		
		for region in self.view.sel():
			theRegionStr = self.view.substr(region)
			self.view.replace(edit, region, self.parseText(theRegionStr))

	def parseText(self, text):
		return re.sub('<', '&lt;', text)