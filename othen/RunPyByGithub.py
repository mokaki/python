
'''
py3

RunPyByGithub
ATW202107140008
mokaki

pip install 

https://stackoverflow.com/questions/54963794/read-python-code-from-github-and-execute-locally



'''
# -*- coding: UTF-8 -*-



import urllib.request

code = 'https://raw.githubusercontent.com/mokaki/AutoWeb/master/%E8%87%AA%E5%8B%95%E6%90%B5%E5%AE%A2.py'

response = urllib.request.urlopen(code)
data = response.read()

exec(data)