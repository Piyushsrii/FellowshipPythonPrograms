class CreateTuple:
    def create(self,rangeVal):
        tupleValue = ( )
        for j in range(rangeVal):
            val = int(input("Enter The Int value for tuple : "))
            tupleValue = tupleValue[ : j] + (val,) + tupleValue[ j : ]
        print("Tuple Data :- ", tupleValue)

tupleData = CreateTuple()
rangeVal = int(input("Enter The range of value you want to enter : "))
tupleData.create(rangeVal)