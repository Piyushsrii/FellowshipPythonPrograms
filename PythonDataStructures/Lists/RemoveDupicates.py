class RemoveDuplicates:
    def remduplicates(self,ListOfNum):
        dupElemnts = set()
        uniqElements = [ ]
        for x in ListOfNum:
            if x not in dupElemnts:
                uniqElements.append(x)
                dupElemnts.add(x)
        print("Updated Element Set : ",dupElemnts)
        print("Updated Element List : ",uniqElements)

listData = RemoveDuplicates()
rangeVal = int(input("Enter The range of value you want to enter : "))
ListOfNum = [ ]
for i in range(1,rangeVal+1):
    val = int(input("Enter The value for List : "))
    ListOfNum.append(val)
print("List Data :- ",ListOfNum)
listData.remduplicates(ListOfNum)