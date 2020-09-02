class CheckElement:
    def checkExist(self,tupleValue,findVal):
        print("Element Exists : ",findVal in tupleValue)

tupleData = CheckElement()
rangeVal = int(input("Enter The range of value you want to enter : "))
tupleValue = ( )
for j in range(rangeVal):
    val = input("Enter The Int value for tuple : ")
    tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
print("Tuple Data :- ", tupleValue)
findVal = input("Enter value you want to Count : ")
tupleData.checkExist(tupleValue,findVal)