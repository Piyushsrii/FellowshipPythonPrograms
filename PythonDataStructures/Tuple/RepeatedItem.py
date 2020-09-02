class RepeatedItem:
    def findRepetedItem(self,tupleValue,findVal):
        countValue = tupleValue.count(findVal)
        print("Count Of Value ",findVal,"Is : ",countValue)


tupleData = RepeatedItem()
rangeVal = int(input("Enter The range of value you want to enter : "))
tupleValue = ( )
for j in range(rangeVal):
    val = int(input("Enter The Int value for tuple : "))
    tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
print("Tuple Data :- ", tupleValue)
findVal = int(input("Enter value you want to Count : "))
tupleData.findRepetedItem(tupleValue,findVal)