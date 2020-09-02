import struct
class CheckShellExec:
    def checkExec(self):
        print("Shell Executing on : ",struct.calcsize("P") * 8,"Bit")

operatingSys = CheckShellExec()
operatingSys.checkExec()
