import requests
resp = requests.request('HEAD', "http://www.mobanwang.com/mb/showsoftdown.asp?urlid=1&softid=18335")



print(resp.headers['content-length'])

