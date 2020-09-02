class CommonItemList:
    def checkCommon(self,ListOfStr1,ListOfStr2):
        print("Common List Are : ",set(ListOfStr1) & set(ListOfStr2))

listData = CommonItemList()
rangeVal1 = int(input("Enter The range of value you want to enter : "))
ListOfStr1 = [ ]
for i in range(1,rangeVal1+1):
    listVal1 = input("Enter the value for List 1: ")
    ListOfStr1.append(listVal1)
rangeVal2 = int(input("Enter The range of value you want to enter : "))
ListOfStr2 = [ ]
for i in range(1,rangeVal2+1):
    listVal2 = input("Enter the value for List 2: ")
    ListOfStr2.append(listVal2)

print("List Data :- ",ListOfStr1,ListOfStr2)
listData.checkCommon(ListOfStr1,ListOfStr2)