from glob import glob
import webbrowser

for file in glob('index.html'):
    webbrowser.open_new_tab(file)
    



import os
os.system("pause")
