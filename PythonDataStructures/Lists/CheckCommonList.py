class CheckCommonList:
    def chkCommon(self,ListOfNum1,ListOfNum2):
        result = False
        for x in ListOfNum1:
            for y in ListOfNum2:
                if x == y:
                    result = True
        return result

listData = CheckCommonList()
rangeVal1 = int(input("Enter The range of value you want to enter : "))
ListOfNum1 = [ ]
for i in range(1,rangeVal1+1):
    listVal1 = int(input("Enter The value for List 1: "))
    ListOfNum1.append(listVal1)
rangeVal2 = int(input("Enter The range of value you want to enter : "))
ListOfNum2 = [ ]
for i in range(1,rangeVal2+1):
    listVal2 = int(input("Enter The value for List 2: "))
    ListOfNum2.append(listVal2)

print("List Data :- ",ListOfNum1,ListOfNum2)
print("Common Data Results Are : ",listData.chkCommon(ListOfNum1,ListOfNum2))