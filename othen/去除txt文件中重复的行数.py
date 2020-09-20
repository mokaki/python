
#coding:utf-8
import shutil
readDir = "88dbDate-生意頂讓202009.txt"
writeDir = "a88dbDate-生意頂讓202009.txt"
lines_seen = set()
outfile=open(writeDir,"w+",encoding='utf-8-sig')
f = open(readDir,"r",encoding='utf-8-sig').readlines()
for line in f:
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print('success')
 