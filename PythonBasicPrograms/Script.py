import sys
class Script:
    def getCmdLinearg(self):
        print("This Name Of the script :", sys.argv[0])
        print("Number of arguments passes :", len(sys.argv))
        print("Argument List : ", str(sys.argv))

arg = Script()
arg.getCmdLinearg()
