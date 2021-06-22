
'''
py3
HowToSaveImagePython3Cv2 
202106220941

pip install os
pip install opencv-python
https://blog.csdn.net/qq_32846595/article/details/79264071
https://appdividend.com/2020/06/23/python-cv2-imwrite-python-cv2-save-image-example/

'''

# importing cv2 module
import cv2
import os


# Using cv2.imread() method to read the image
img = cv2.imread('8.jpg')



# Using cv2.imwrite() method saving the image
cv2.imwrite('saeewqved_new.jpg', img)

print('The image is saved Successfully')
print('按鍵退出程式')
os.system("pause")


