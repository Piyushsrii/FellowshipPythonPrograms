class RetLongString:
    def chkLongString(self, listOfStr):
        wordLength = [ ]
        for n in listOfStr:
            wordLength.append((len(n), n))
        wordLength.sort()
        return wordLength[-1][1]

stringData = RetLongString()
rangeVal = int(input("Enter The range of value you want to enter : "))
listOfStr = []
for i in range(1, rangeVal + 1):
    strVal = input("Enter The Words In List : ")
    listOfStr.append(strVal)

print("List Of String :- ", listOfStr)
print("The Longest String Are : ", stringData.chkLongString(listOfStr))