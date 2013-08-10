import sublime, sublime_plugin
import webbrowser
from sys import version_info as python_version

if int(python_version[0]) >= 3:
	import urllib.parse as urlparser
else:
	import urllib as urlparser


class PhpFuncHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		url = 'http://www.php.net/manual/en/function.'

		selected = self.view.sel()
		function_name = self.view.substr(selected[0]).strip()

		if function_name != '':
			url_to_open = url + urlparser.quote_plus(function_name) + '.php'
		else:
			url_to_open = url + urlparser.quote_plus(function_name) + '.php'

		webbrowser.open_new_tab(url_to_open)
