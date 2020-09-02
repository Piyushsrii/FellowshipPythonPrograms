class ListToDictionary:
    def toDictionary(self,ListOfNum):
        newDict = currentDict = { }
        for new in ListOfNum:
            currentDict[new] = { }
            currentDict = currentDict[new]
        print(newDict)

listData = ListToDictionary()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for dictionary : "))
    ListOfNum.append(val)

listData.toDictionary(ListOfNum)