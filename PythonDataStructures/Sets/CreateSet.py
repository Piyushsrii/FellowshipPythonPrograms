class CreateSet:
    def create(self,dictOfNum):
        emptySet = set()
        print("Empty Set : ", emptySet)

        nonEmptySet = set(dictOfNum)
        print("Non Empty Set : ", nonEmptySet)

rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = [ ]
for i in range(1,rangeVal+1):
    val = input("Enter The value : ")
    dictOfNum.append(val)
setData = CreateSet()
setData.create(dictOfNum)