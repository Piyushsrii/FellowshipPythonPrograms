import os
class EnvironmentVariables:

    def envAccess(self):
        #For Checking all environment variables
        print('*----------------------------------*')
        print(os.environ)
        print('*----------------------------------*')
    def checkEnv(self, envName):
       	# For Checking a particular environment variable
        print (envName)
        print(os.environ[envName])
        print('*----------------------------------*')

envObj = EnvironmentVariables()
envObj.envAccess()
envName = input("Enter Environment Name : ")
envObj.checkEnv(envName)
