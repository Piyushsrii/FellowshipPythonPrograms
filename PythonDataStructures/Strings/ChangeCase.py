class ChangeCase:
    def toUpperCAse(self,strVal):
        print(strVal.upper())

    def toLowerCAse(self,strVal):
        print(strVal.lower())

stringData = ChangeCase()
strVal = input("Enter A String : ")
stringData.toLowerCAse(strVal)
stringData.toUpperCAse(strVal)