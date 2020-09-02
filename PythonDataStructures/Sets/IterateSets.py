class IterateSets:
    def toIterate(self,dictOfNum):
        numItrSet = set(dictOfNum)
        for n in numItrSet:
            print(n)

rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = []
for i in range(1, rangeVal + 1):
    val = input("Enter The value : ")
    dictOfNum.append(val)
setData = IterateSets()
setData.toIterate(dictOfNum)