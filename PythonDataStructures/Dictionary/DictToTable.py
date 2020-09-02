class DictToTable:
    def toTable(self,mulDictionary):
        for row in zip(*([key] + (value) for key, value in sorted(mulDictionary.items()))):
            print(" ", *row)

dictValues = DictToTable()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    valArr = [ ]
    for i in range(1, rangeVal + 1):
        val = int(input("Enter The value for dictionary : "))
        valArr.append(val)
    dictOfNum.setdefault(key, valArr)
print (dictOfNum)
dictValues.toTable(dictOfNum)
