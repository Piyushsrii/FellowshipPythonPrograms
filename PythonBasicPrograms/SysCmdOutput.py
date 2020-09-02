import subprocess
class SystemCmdOutPut:
    def output(self):
        # file and directory listing
        returnTxt = subprocess.check_output("dir", shell=True, universal_newlines=True)
        print(returnTxt)

command = SystemCmdOutPut()
command.output()