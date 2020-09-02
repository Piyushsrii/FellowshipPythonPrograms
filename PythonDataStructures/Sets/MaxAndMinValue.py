class ManAndMinValue:
    def printMaxMin(self, setValue):
        print("Maximum Value are : ",max(setValue))
        print("Minimum Value are : ",min(setValue))


setValue = set()
rangeVal = int(input("Enter The Range Of Values You Want To Enter In Set: "))
for i in range(1, rangeVal + 1):
    valAdd = int(input("Enter The String Or Value : "))
    setValue.add(valAdd)
print("Data Set : ", setValue)
setData = ManAndMinValue()
setData.printMaxMin(setValue)