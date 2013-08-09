import sublime, sublime_plugin
import webbrowser
import urllib

class PhpFuncHelpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		url = 'http://www.php.net/manual/en/function.'

		selected = self.view.sel()
		function_name = self.view.substr(selected[0]).strip()

		if function_name != '':
			url_to_open = url + urllib.quote_plus(function_name) + '.php'
			webbrowser.open_new_tab(url_to_open)
