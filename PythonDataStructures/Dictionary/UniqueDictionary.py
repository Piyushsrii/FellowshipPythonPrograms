class UniqueDictionary:
    def unique(self, dictSet):
        print("Dictionary : ", dictSet)
        uniqueValue = set(val for dic in dictSet for val in dic.values())
        print("Unique Dictionary: ", uniqueValue)

dictValue = UniqueDictionary()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = {}
for i in range(1,rangeVal+1):
    key = input("Enter The Key : ")
    val = input("Enter The value for dictionary : ")
    dictOfNum.setdefault(key, val)

dictSet = [dictOfNum]
print(dictSet)
dictValue.unique(dictSet)





