from os import listdir
from os.path import isfile
class ListFiles:
    def file(self):
        filesList = [ ]
        for f in listdir('./'):
            if isfile(f):
                filesList.append(f)
        print(filesList)

fileObj = ListFiles()
fileObj.file()
