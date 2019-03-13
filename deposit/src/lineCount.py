# Evan DePosit
# program counts lines of code and comment in .c or .py file
# enter how many files you want it to check, then enter the file names.

import string
import re

codeCount=0
commentCount=0

pyCommentPat='\s*#'
cCommentPat='\s*//'
pat=pyCommentPat

fileNum= int(input("Enter number of files: "))
filePathList=[]

for i in range(0, fileNum):
    filePath=input("Enter file name: ")
    filePathList.append(filePath)

for fileName in filePathList:
    
    if '.py' in fileName[-3::1]:
        pat=pyCommentPat
    elif '.c' in fileName[-2::1]:
        pat=cCommentPat
    elif '.cpp' in fileName[-4::1]:
        pat=cCommentPat
    else:
        print('filetype not supported')

    fin = open(fileName, 'rt')
    while True:
        #read in each student by line and count total
        line= fin.readline()
        if line:
            found = re.match(pat, line)
            if found:
               commentCount= commentCount +1
               #print(line) 
            else:
                codeCount = codeCount+1
        if not line:
            break
    fin.close()

print('lines of code= ', codeCount)
print('lines of comment= ', commentCount)

