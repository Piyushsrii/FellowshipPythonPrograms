class CountStrings:
    def matchCharacter(self,listOfStr):
        countStr = 0
        for Str in listOfStr:
            if len(Str) > 1 and Str[0] == Str[-1]:
                countStr += 1
        print("The String Count Whos First And Last Char Is Same Are : ",countStr)

listData = CountStrings()
rangeVal = int(input("Enter The range of value you want to enter : "))
listOfStr = [ ]
for i in range(1,rangeVal+1):
    val = input("Enter The value for List in Strings : ")
    listOfStr.append(val)
print("List Data :- ",listOfStr)
listData.matchCharacter(listOfStr)