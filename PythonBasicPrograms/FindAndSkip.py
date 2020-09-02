import os
class FindAndSkip:
    def checkfiles(self):
        for f in os.listdir('./'):
            if os.path.isfile(f):
                result = os.path.join(f)
                print (result)

directory = FindAndSkip()
directory.checkfiles()

