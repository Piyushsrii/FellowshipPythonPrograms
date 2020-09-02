class DiffDateType:
    def createDiffType(self,intVal,floatVal,strVal,boolVal):
        tupleValue = (intVal, floatVal, strVal, boolVal)
        print("Tuple Data :- ", tupleValue)

tupleData = DiffDateType()
intVal = int(input("Enter The Int Value : "))
floatVal = float(input("Enter The Float Value : "))
strVal = input("Enter A String  : ")
boolVal = bool(input("Enter The Boolean Value True or False : "))
tupleData.createDiffType(intVal,floatVal,strVal,boolVal)