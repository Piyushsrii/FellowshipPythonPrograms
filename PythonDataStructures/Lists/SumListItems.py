class SumListItems:
    def toSum(self,ListOfNum):
        sum = 0
        for x in ListOfNum:
            sum += x
        print("Sum Of List is : ",sum)

listData = SumListItems()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for List : "))
    ListOfNum.append(val)
print("List Data :- ",ListOfNum)
listData.toSum(ListOfNum)