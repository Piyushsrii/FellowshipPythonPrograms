import os.path, time
class File:
    def creationTime(self,fileName):
        print("Created On : %s" % time.ctime(os.path.getctime(fileName)))
    def modificationTime(self,fileName):
        print("Modified on : %s" % time.ctime(os.path.getmtime(fileName)))

fileMods = File()
fileName = input("Enter The Name Of The File With Extension : ")
fileMods.creationTime(fileName)
fileMods.modificationTime(fileName)
