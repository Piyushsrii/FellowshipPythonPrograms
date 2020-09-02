class ClearSet:
    def toClear(self, setValue):
        copySet = setValue.copy()
        print("Copy Set : ",copySet)
        copySet.clear()
        print("Clear Set : ",copySet)

setValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(1, rangeVal + 1):
    valAddFirst = input("Enter The String Or Value : ")
    setValue.add(valAddFirst)
print("Data Set First: ", setValue)

setData = ClearSet()
setData.toClear(setValue)