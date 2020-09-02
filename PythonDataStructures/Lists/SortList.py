class SortList:
    def lastElement (tupleValue):
        return tupleValue[-1]

    def sortAsc(self,ListOfNum):
        print("Sorted List : ",sorted(ListOfNum, key=SortList.lastElement))

listData = SortList()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    tupleValue = ( )
    for j in range(2):
        val = int(input("Enter The value for tuple : "))
        tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
    ListOfNum.append(tupleValue)

print("List Data :- ",ListOfNum,tupleValue)
listData.sortAsc(ListOfNum)