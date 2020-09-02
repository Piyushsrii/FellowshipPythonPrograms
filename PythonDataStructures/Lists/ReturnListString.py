class ReturnListString:
    def wordsLongList(self,listOfStr,lenValue):
        newWords = []
        for x in listOfStr:
            if len(x) > lenValue:
                newWords.append(x)
        return newWords

listData = ReturnListString()
rangeVal = int(input("Enter The range of value you want to enter : "))
listOfStr = [ ]
for i in range(1,rangeVal+1):
    strVal = input("Enter The Words In List : ")
    listOfStr.append(strVal)
print("List Data :- ",listOfStr)
lenValue = int(input("Enter the length of words value you want to find : "))
newLenWords = listData.wordsLongList(listOfStr,lenValue)
print("The New Length Words in List Are : ",newLenWords)