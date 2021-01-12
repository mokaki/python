

url = 'http://www.mobanwang.com/mb/showsoftdown.asp?urlid=1&softid=18061'
 
# downloading with requests
 
# import the requests library
import requests
 




# download the file contents in binary format
r = requests.get(url)
 
# open method to open a file on your system and write the contents
with open("18061w.rar", "wb") as code:
	
	code.write(r.content)

 
# downloading with urllib
 
# import the urllib library
import urllib
 
# Copy a network object to a local file
urllib.urlretrieve(url, "18061w.rar")