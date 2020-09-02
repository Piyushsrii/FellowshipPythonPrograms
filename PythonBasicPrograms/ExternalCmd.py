from subprocess import call
class ExternalCmd:
    def checkCmd(self,inputCmd):
        listValue = inputCmd.split(" ")
        call(listValue)

inputCmd = input("Enter The Command  : ")
cmdObj = ExternalCmd()
cmdObj.checkCmd(inputCmd)
