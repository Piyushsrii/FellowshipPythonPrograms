class MinListItems:
    def findMin(self,ListOfNum):
        min = ListOfNum[0]
        for x in ListOfNum:
            if x < min:
                min = x
        print("Smallest Number in List Items is : ",min)

listData = MinListItems()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for List : "))
    ListOfNum.append(val)
print("List Data :- ",ListOfNum)
listData.findMin(ListOfNum)