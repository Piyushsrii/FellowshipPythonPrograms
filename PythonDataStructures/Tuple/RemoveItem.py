class RemoveItem:
    def toRemoveItem(self,tupleValue,remVal,indexVal):
        tupleValue = tupleValue[:indexVal] + tupleValue[indexVal+1:]
        print("Using Merging Removed Value : ",tupleValue)
        listTuple = list(tupleValue)
        listTuple.remove(remVal)
        tupleValue = tuple(listTuple)
        print("Using Conversion Removed Value : ",tupleValue)

tupleData = RemoveItem()
rangeVal = int(input("Enter The range of value you want to enter : "))
tupleValue = ( )
for j in range(rangeVal):
    val = input("Enter The Int value for tuple : ")
    tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
print("Tuple Data :- ", tupleValue)
indexVal = int(input("Enter index value you want to Remove : "))
remVal = input("Enter value you want to Remove : ")
tupleData.toRemoveItem(tupleValue,remVal,indexVal)