import webbrowser
import sys
import pyperclip
#webbrowser.open('www.google.com')

arg_list = sys.argv #['webbrowser_demos.py', '870', 'Valencia', 'St.']
if len(arg_list) > 1:
    address = ' '.join(arg_list[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)