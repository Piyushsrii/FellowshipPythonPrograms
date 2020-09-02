import os.path
class checkFile:
    def checkFile(self,fileName):
        print(os.path.exists('./fileName'))

fileObj = checkFile()
fileName = input("Enter The Name Of The File With Extension In This Format ./fileName : ")
fileObj.checkFile(fileName)
