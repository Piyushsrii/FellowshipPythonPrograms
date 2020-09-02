class ListToTuple:
    def toTuple(self,ListOfNum):
        tupleOfNum = tuple(ListOfNum)
        print("Tuple Data : ",tupleOfNum)

listData = ListToTuple()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for tuple : "))
    ListOfNum.append(val)

print("List Data :- ",ListOfNum)
listData.toTuple(ListOfNum)