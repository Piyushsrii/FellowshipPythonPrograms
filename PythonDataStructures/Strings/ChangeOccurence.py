class ChangeOccurence:
    def chkOccurence(self,strVal):
        char = strVal[0]
        strVal = strVal.replace(char, '$')
        strVal = char + strVal[1:]

        return strVal

stringData = ChangeOccurence()
strVal = input("Enter A String : ")
print("String Character Count is : ",stringData.chkOccurence(strVal))