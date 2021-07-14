

'''
py3
使用Python下載文件示例
ATW202107141344
mokaki
pip install 
#https://gist.github.com/oculushut/193a7c2b6002d808a791
'''




import urllib.request
url = "https://raw.githubusercontent.com/mokaki/AutoWeb/master/%E8%87%AA%E5%8B%95%E6%90%B5%E5%AE%A2(RSA%E8%B6%85%E8%BF%8753%E4%B8%AA%E5%AD%97).py"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename="aaa12332341_.py")
print ("download complete!")
print ("download file location: ", filename)
print ("download headers: ", headers)

