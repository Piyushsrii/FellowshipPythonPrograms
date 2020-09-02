class MulListItems:
    def toMul(self,ListOfNum):
        sum = 1
        for x in ListOfNum:
            sum *= x
        print("Multiplication Of List Items is : ",sum)

listData = MulListItems()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for List : "))
    ListOfNum.append(val)
print("List Data :- ",ListOfNum)
listData.toMul(ListOfNum)