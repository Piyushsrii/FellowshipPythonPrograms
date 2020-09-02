class CloningList:
    def getClone(self,ListOfNum):
        cloneList = list(ListOfNum)
        print("Original List : ",ListOfNum)
        print("Clone List : ",cloneList)

listData = CloningList()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for List : "))
    ListOfNum.append(val)
listData.getClone(ListOfNum)