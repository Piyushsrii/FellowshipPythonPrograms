class DiffInList:
    def chkDiff(self,ListOfNum1,ListOfNum2):
        diffList1List2 = list(set(ListOfNum1) - set(ListOfNum2))
        diffList2List1 = list(set(ListOfNum2) - set(ListOfNum1))
        total_diff = diffList1List2 + diffList2List1
        return total_diff

listData = DiffInList()
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
print("Difference In List Are : ",listData.chkDiff(ListOfNum1,ListOfNum2))