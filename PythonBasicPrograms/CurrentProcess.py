import os
class CurrentProcess:
    def process(self):
        print("\nEffective Group Id: ", os.getegid())
        print("Effective User Id: ", os.geteuid())
        print("Real Group Id: ", os.getgid())
        print("List Of Supplemental Group Ids: ", os.getgroups(),"\n")

current = CurrentProcess()
current.process()
