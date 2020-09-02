class FrozenSets:
    def frozen(self, firstSetValue, SecondSetValue):
        #Return True if the set has no elements in common with other.
        print("No Common Elements : ",firstSetValue.isdisjoint(SecondSetValue))
        #Return a new set with elements in the set that are not in the others.
        print("Set Difference Elements : ",firstSetValue.difference(SecondSetValue))
        #New set with elements from both
        print("All Elements : ",firstSetValue | SecondSetValue)

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

setData = FrozenSets()
setData.frozen(firstSetValue, SecondSetValue)