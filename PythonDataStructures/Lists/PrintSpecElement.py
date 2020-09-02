class PrintSpecElement:
    def wordsLongList(self,listOfStr):
        listOfStr = [x for (i, x) in enumerate(listOfStr) if i not in (0, 4, 5)]
        return listOfStr

listData = PrintSpecElement()
rangeVal = int(input("Enter The range of value you want to enter : "))
listOfStr = [ ]
for i in range(1,rangeVal+1):
    strVal = input("Enter The Words In List : ")
    listOfStr.append(strVal)

print("List Data :- ",listOfStr)
print("The Updated List Are : ",listData.wordsLongList(listOfStr))