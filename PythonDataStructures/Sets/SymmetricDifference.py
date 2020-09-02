class SymmetricDifference:
    def symmetricDiff(self, firstSetValue, SecondSetValue):
        symmDiffSet = firstSetValue ^ SecondSetValue
        print("Difference in Set : ", symmDiffSet)

firstSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(1, rangeVal + 1):
    valAddFirst = input("Enter The String Or Value : ")
    firstSetValue.add(valAddFirst)

SecondSetValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In First Set: "))
for i in range(1, rangeVal + 1):
    valAddSecond = input("Enter The String Or Value : ")
    SecondSetValue.add(valAddSecond)

print("Data Set First: ", firstSetValue)
print("Data Set Second: ", SecondSetValue)

setMembers = SymmetricDifference()
setMembers.symmetricDiff(firstSetValue, SecondSetValue)