import getpass
class CurrentUser:
    def checkUser(self):
        print(getpass.getuser())

userObj = CurrentUser()
userObj.checkUser()

