
﻿
'''
py3
RunPyByGithub
ATW202107151846
mokaki
pip install 
https://stackoverflow.com/questions/54963794/read-python-code-from-github-and-execute-locally
'''
# -*- coding: UTF-8 -*-


# RunPyByGithub
import urllib.request
code = 'https://raw.githubusercontent.com/mokaki/AutoWeb/master/.py/_1AutoWebProfile.py'
response = urllib.request.urlopen(code)
data = response.read()

# send vlo
import sys
sys.path.append(data)
import _1AutoWebProfile
qweq = _1AutoWebProfile.LoginATW('您們')
#



