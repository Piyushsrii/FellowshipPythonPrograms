import os
class AbsolutePath:
    def absFilePath(self,filename):
        return os.path.abspath(filename)

pathObj = AbsolutePath()
fileName = input("Enter The Name Of The File With Extension : ")
print("Absolute file path: ", pathObj.absFilePath(fileName))