class AppendList:
    def setAppend(self,ListOfNum1,ListOfNum2):
        appendList = ListOfNum1 + ListOfNum2
        return appendList

listData = AppendList()
rangeVal1 = int(input("Enter The range of value you want to enter : "))
ListOfNum1 = [ ]
for i in range(1,rangeVal1+1):
    listVal1 = int(input("Enter The Integer value for List 1: "))
    ListOfNum1.append(listVal1)
rangeVal2 = int(input("Enter The range of value you want to enter : "))
ListOfNum2 = [ ]
for i in range(1,rangeVal2+1):
    listVal2 = input("Enter The String value for List 2: ")
    ListOfNum2.append(listVal2)

print("List Data :- ",ListOfNum1,ListOfNum2)
print("Difference In List Are : ",listData.setAppend(ListOfNum1,ListOfNum2))