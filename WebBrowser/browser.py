import webbrowser
#
# webbrowser.open("https://www.python.org", new=1)
#
# help(webbrowser)
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path), 1)
chrome = webbrowser.get('chrome').open_new_tab("https://www.python.org/")
