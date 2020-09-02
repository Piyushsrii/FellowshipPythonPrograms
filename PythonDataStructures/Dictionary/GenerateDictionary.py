class GenerateDictionary:
    def generate(self, dictOfNum,rangeVal):
        for i in range(1, rangeVal + 1):
            dictOfNum[i] = i * i
        print(dictOfNum)

dictionary = GenerateDictionary()
rangeVal = int(input("Enter The range of value you want to enter : "))
dictOfNum = { }
dictionary.generate(dictOfNum,rangeVal)
