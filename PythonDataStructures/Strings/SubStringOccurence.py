class SubStringOccurence:
    def countOccurence(self,strVal,subString):
        print("The Count Of SubString ",subString," is : ",strVal.count(subString))

stringData = SubStringOccurence()
strVal = input("Enter a string : ")
subString = input("Enter a substring to count : ")
stringData.countOccurence(strVal,subString)

