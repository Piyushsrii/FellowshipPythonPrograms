import os

class UserEnvironment:
    def getEnv(self):
        print(os.environ)

user = UserEnvironment()
user.getEnv()