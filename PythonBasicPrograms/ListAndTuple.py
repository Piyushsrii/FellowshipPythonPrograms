class ListAndTuple:
    def __init__(self, value):
        self.value = value

    def splitValue(self):
        listValue = self.value.split(",")
        tupleValue = tuple(listValue)
        print('List : ', listValue)
        print('Tuple : ', tupleValue)


inputValues = input("Input some comma seprated numbers : ")

valueObj = ListAndTuple(inputValues)
valueObj.splitValue()

