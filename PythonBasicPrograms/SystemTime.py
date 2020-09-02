import time
class SystemTime:
    def getTime(self):
        print(time.ctime())

system = SystemTime()
system.getTime()