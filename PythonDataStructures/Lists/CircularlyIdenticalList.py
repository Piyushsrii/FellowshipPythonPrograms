class CircularlyIdenticalList:
    def chkCircIdentical(self,ListOfNum1,ListOfNum2):
        print("list1 and list2 are ciruclary identical : ",' '.join(map(str, ListOfNum1)) in ' '.join(map(str, ListOfNum2 * 2)))

listData = CircularlyIdenticalList()
rangeVal1 = int(input("Enter The range of value you want to enter : "))
ListOfNum1 = [ ]
for i in range(1,rangeVal1+1):
    listVal1 = input("Enter the value for List 1: ")
    ListOfNum1.append(listVal1)
rangeVal2 = int(input("Enter The range of value you want to enter : "))
ListOfNum2 = [ ]
for i in range(1,rangeVal2+1):
    listVal2 = input("Enter the value for List 2: ")
    ListOfNum2.append(listVal2)

print("List Data :- ",ListOfNum1,ListOfNum2)
listData.chkCircIdentical(ListOfNum1,ListOfNum2)