class ReverseTuple:
    def toReverse(self,tupleValueInt,tupleValueStr):
        revrseIntTuple = reversed(tupleValueInt)
        print("Revserse Tuple Integer: ",tuple(revrseIntTuple))

        revrseStrTuple = reversed(tupleValueStr)
        print("Revserse Tuple String: ", tuple(revrseStrTuple))

tupleData = ReverseTuple()
rangeVal = int(input("Enter The range of value : "))
tupleValueInt = ( )
for j in range(rangeVal):
    val = int(input("Enter The Int value for tuple : "))
    tupleValueInt = tupleValueInt[ : j] + (val,) + tupleValueInt[ j : ]

rangeVal = int(input("Enter The range of value : "))
tupleValueStr = ( )
for i in range(rangeVal):
    val = input("Enter a String : ")
    tupleValueStr = tupleValueStr[ : i] + (val,) + tupleValueStr[ i : ]

print("Tuple Data :- ", tupleValueInt,tupleValueStr)
tupleData.toReverse(tupleValueInt,tupleValueStr)

