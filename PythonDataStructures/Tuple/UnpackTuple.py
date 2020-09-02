class UnpackTuple:
    def unpackVariables(self,rangeVal):
        tupleValue = ( )
        for j in range(rangeVal):
            val = int(input("Enter The Int value for tuple : "))
            tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
        print("Tuple Data :- ", tupleValue)
        try:
            if len(tupleValue) == 3:
                n1, n2, n3 = tupleValue
                print(n1 + n2 + n3)
            elif len(tupleValue) == 4:
                n1, n2, n3, n4 = tupleValue
                print(n1 + n2 + n3 + n4)
            else:
                n1, n2, n3, n4, n5 = tupleValue
                print(n1 + n2 + n3 + n4 + n5)
        except ValueError:
            print("the number of variables must be equal to the number of items of the tuple")

tupleData = UnpackTuple()
rangeVal = int(input("Enter The range more than 2 and less than or equal to 5 : "))
tupleData.unpackVariables(rangeVal)