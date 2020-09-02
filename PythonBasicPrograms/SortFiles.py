import glob
import os
class SortFiles:
    def checkFile(self):
        files = glob.glob('*.py')
        files.sort(key=os.path.getmtime)
        print("\n".join(files))

fileObj = SortFiles()
fileObj.checkFile()




