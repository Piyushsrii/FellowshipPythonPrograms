class SliceTuple:
    def toSlice(self,tupleValueInt,tupleValueStr):
        print("Original Set : ",tupleValueInt)
        sliceTuple = tupleValueInt[3:5]
        print("Printing From 3 to 4 : ",sliceTuple)
        sliceTuple = tupleValueInt[:6]
        print("Printing From 0 to 5 : ",sliceTuple)
        sliceTuple = tupleValueInt[5:]
        print("Printing From 5 to End ",sliceTuple)
        sliceTuple = tupleValueInt[:]
        print("Printing when index is not known",sliceTuple)
        sliceTuple = tupleValueInt[-8:-4]
        print("Printing From Left Side From -8 to -5",sliceTuple)
        print("Original Set String : ",tupleValueStr)
        sliceTuple = tupleValueStr[::4]
        print(sliceTuple)
        tupleValueStrs = tuple("Hello World")
        sliceTuple = tupleValueStrs[2:9:2]
        print(sliceTuple)
        sliceTuple = tupleValueStrs[::4]
        print(sliceTuple)
        sliceTuple = tupleValueStrs[9:2:-4]
        print(sliceTuple)


tupleData = SliceTuple()
rangeVal = int(input("Enter The range Between 5 to 10 : "))
tupleValueInt = ( )
for j in range(rangeVal):
    val = int(input("Enter The Int value for tuple : "))
    tupleValueInt = tupleValueInt[ : j] + (val,) + tupleValueInt[ j : ]

rangeVal = int(input("Enter The range of value you want to enter : "))
tupleValueStr = ( )
for i in range(rangeVal):
    val = input("Enter a String : ")
    tupleValueStr = tupleValueStr[ : i] + (val,) + tupleValueStr[ i : ]

print("Tuple Data :- ", tupleValueInt,tupleValueStr)
tupleData.toSlice(tupleValueInt,tupleValueStr)