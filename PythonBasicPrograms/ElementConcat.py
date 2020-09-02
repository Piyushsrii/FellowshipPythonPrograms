class ElementConcat:
    def concatenateData(self,listOfValues):
        resultStr = ''
        for element in listOfValues:
            resultStr += str(element)
        return resultStr

listOfInt = []
rangeOfValue = int(input("Enter The Range Of Values You Want To Enter : "))
for i in range(rangeOfValue):
    value = int(input("Enter The Value : "))
    listOfInt.append(value)

print(listOfInt)
listObj = ElementConcat()
print(listObj.concatenateData(listOfInt))
