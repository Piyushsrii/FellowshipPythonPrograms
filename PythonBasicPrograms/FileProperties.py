import os.path
import time
class FileProperties:
    def getProperties(self):
        print('File         :', __file__)
        print('Access time  :', time.ctime(os.path.getatime(__file__)))
        print('Modified time:', time.ctime(os.path.getmtime(__file__)))
        print('Change time  :', time.ctime(os.path.getctime(__file__)))
        print('Size         :', os.path.getsize(__file__))

file = FileProperties()
file.getProperties()
